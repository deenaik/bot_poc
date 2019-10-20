from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import SlotSet

class ActionIdentifyTicketAttributes(Action):

    def name(self) -> Text:
        return "action_identify_ticket_attributes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         dispatcher.utter_message("Priority: High and Category: Network Issue")
         return [SlotSet("priority", "High"),SlotSet("category", "Network Issue")]


class ActionLogTicket(Action):

    def name(self) -> Text:
        return "action_log_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         dispatcher.utter_message("Ticket logged successfully! :)")
         return []
