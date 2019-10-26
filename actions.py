from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import REQUESTED_SLOT
from rasa_sdk.forms import SlotSet, FormAction
import requests
import yaml
from slackclient import SlackClient
import re
from joblib import load
from chatterbot import ChatBot
from rasa.core.policies.fallback import FallbackPolicy

class SmallTalks:
    chatbot = ChatBot("SmallTalk",logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                        'chatterbot.logic.UnitConversion',
                                        'chatterbot.logic.BestMatch'])

    @staticmethod
    def response(text):
        return SmallTalks.chatbot.get_response(text).text


class ActionIdentifyTicketAttributes(Action):
    __priority_model = None
    __category_model = None

    def __init__(self):
        self.__priority_model = load('classifier/priority_model.pkl')
        self.__category_model = load('classifier/category_model.pkl')

    def name(self) -> Text:
        return "action_identify_ticket_attributes"

    def clean_text(self, text):
        # remove backslash-apostrophe
        text = re.sub("\'", "", text)
        # remove everything except alphabets
        text = re.sub("[^a-zA-Z]", " ", text)
        # remove whitespaces
        text = ' '.join(text.split())
        # convert text to lowercase
        text = text.lower()

        return text


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         message = tracker.latest_message.get('text')
         if message and str(message).strip():
             message = self.clean_text(message)
             priority = self.__priority_model.predict([message])[0]
             category = self.__category_model.predict([message])[0]
             return [SlotSet("priority", priority), SlotSet("category", category)]
         print(self.name())
         return []


class ActionLogTicket(Action):

    def name(self) -> Text:
        return "action_log_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          return[SlotSet('message',tracker.latest_message.get('text'))]


class ActionLogTicket(Action):

    def name(self) -> Text:
        return "action_log_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          ticket_attributes = {}
          for key, value in tracker.current_slot_values().items():
              if value:
                  ticket_attributes[key] = value

          response = requests.post('http://dummy_rest/Tickets/ticket', json=json.dumps(ticket_attributes))
          response_text = json.loads(response.text)
          dispatcher.utter_message(response_text['ticketID'] + " has been logged successfully :simple_smile:")
          return[]

class ActionResetSlots(Action):

    def name(self) -> Text:
        return "action_reset_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         print(self.name())
         return [AllSlotsReset()]


class ActionClearMemory(Action):

    def name(self) -> Text:
        return "action_clear_memory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         print(self.name())
         return [AllSlotsReset(), Restarted()]

class ActionGetTicketStatus(Action):

    def name(self) -> Text:
        return "action_get_ticket_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Your ticket is currently *under analysis*. \nDue date for ticket resolution is *30-Oct-2019*")
        print(self.name())
        return []


class FormTicketAttributes(FormAction):

    def name(self) -> Text:
        return "ticket_attributes_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["priority"]

    def slot_mappings(self):
        return {
            "priority": [self.from_entity(entity="priority",intent="get_priority")]
        }

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                return []

        for slot, value in slot_values.items():
            if value not in ["Critical","High", "Medium", "Low"]:
                return []
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        print(self.name())
        return []

class FormTicketFile(FormAction):

    def name(self) -> Text:
        return "ticket_file_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["file"]

    def slot_mappings(self):
        return {
            "file": [self.from_entity(entity="file",intent="file_upload_json")],
            "file_text": [self.from_entity(entity="file_text", intent="file_upload_json")]
        }

    def get_file_link(self, file_name):
        data = None
        error = None
        if file_name:
            token = self.load_credential()['slack']['slack_user_token']
            slack_client = SlackClient(token)
            req_json = slack_client.api_call("files.sharedPublicURL",file=file_name)
            if "file" in req_json:
                data = req_json['file']['url_private_download']
            else:
                data = file_name
                if "error" in req_json:
                    error = req_json['error']
        return (data,error)

    def load_credential(self):
        with open("credentials.yml") as fp:
            data = yaml.load(fp, Loader=yaml.FullLoader)
        return data

    def fill_slot(self,text):
        try:
            file = json.loads(text)
            print(file['file'])
            if file['file']:
                data, error = self.get_file_link(file['file'])
                return [SlotSet('file',data), SlotSet('file_text', file['file_text']), SlotSet('file_error',error)]
            else:
                return []
        except Exception as e:
            print(e)
            return []

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        print(slot_to_fill)
        if slot_to_fill:
            return self.fill_slot(tracker.latest_message.get('text'))
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        print(self.name())
        return []

class ActionValidateTicketForUpload(Action):

    def name(self) -> Text:
        return "action_validate_ticket_for_fileUpload"

    def slot_mappings(self):
        return {
            "ticketID": [self.from_entity(entity="ticketID",intent="get_ticketID")]
        }

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get('http://dummy_rest/Tickets/ticket', json=json.dumps(tracker.get_slot('ticketID')))
        print(response.content.decode('utf8'))
        print(response.text)
        dispatcher.utter_message(response.text)
        # dispatcher.utter_template("utter_invalid_ticketID", tracker)
        # dispatcher.utter_template("utter_ask_file", tracker)
        print(self.name())
        return []

class ActionValidateTicketForStatus(Action):

    def name(self) -> Text:
        return "action_validate_ticket_for_status"

    def slot_mappings(self):
        return {
            "ticketID": [self.from_entity(entity="ticketID",intent="get_ticketID")]
        }

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ticket_attributes = {}
        ticket_attributes['ticketID'] = tracker.get_slot('ticketID')

        response = requests.get('http://dummy_rest/Tickets/ticket', json=json.dumps(ticket_attributes))
        response_text = json.loads(response.text)
        #if (response_text['status'] == 'Invalid Ticket Number'):
        #    dispatcher.utter_template("utter_invalid_ticketID", tracker)
        #else:
        dispatcher.utter_message("Your ticket is currently " + response_text['status'] + ".\nDue date for ticket resolution is 30-Oct-2019.")
        print(self.name())
        return []

class ActionClearPriority(Action):

    def name(self) -> Text:
        return "action_clear_priority"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(self.name())
        return [SlotSet('priority', None)]

class ActionClearFile(Action):

    def name(self) -> Text:
        return "action_clear_file"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(self.name())
        return [SlotSet('file',None)]


class ActionSmallTalk(Action):

    def name(self) -> Text:
        return "action_small_talk"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(SmallTalks.response(tracker.latest_message.get('text')))
        return []