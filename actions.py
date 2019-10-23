from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, ActionExecutionRejection
from rasa_sdk.events import Restarted, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import SlotSet, FormAction
from rasa_sdk.forms import REQUESTED_SLOT

class ActionIdentifyTicketAttributes(Action):

    def name(self) -> Text:
        return "action_identify_ticket_attributes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         print(self.name())
         return [SlotSet("priority", "High")]


class ActionLogTicket(Action):

    def name(self) -> Text:
        return "action_log_ticket"

    def forget(self, slots: Dict[Text, Any]):
        for key, value in slots.items():
            slots[key] = None

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          print(tracker.current_state())
          dispatcher.utter_message("Ticket logged successfully! :)")
          return[]

class ActionFileUpload(Action):

    def name(self) -> Text:
        return "action_file_upload"

    def forget(self, slots: Dict[Text, Any]):
        for key, value in slots.items():
            slots[key] = None

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          print(tracker.current_state())
          dispatcher.utter_template("utter_upload_successful", tracker)
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
        dispatcher.utter_message("Your ticket is currently “under analysis”. Due date for ticket resolution is 30-Oct-2019.")
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
        print(slot_to_fill)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        print(self.name())
        dispatcher.utter_template("utter_change_priority", tracker)
        return []

class FormTicketFile(FormAction):

    def name(self) -> Text:
        return "ticket_file_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["file"]

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
        print(slot_to_fill)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        print(self.name())
        dispatcher.utter_template("utter_form_ticket_attributes", tracker)
        return []

class ActionValidateTicket(Action):

    def name(self) -> Text:
        return "action_validate_ticket"

    def slot_mappings(self):
        return {
            "ticketID": [self.from_entity(entity="ticketID",intent="get_ticketID")]
        }

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("ticketID") == "TKT4566":
            dispatcher.utter_template("utter_invalid_ticketID", tracker)
        else:
            dispatcher.utter_template("utter_click_upload", tracker)
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

        if tracker.get_slot("ticketID") == "TKT4566":
            dispatcher.utter_template("utter_invalid_ticketID", tracker)
        print(self.name())
        return []