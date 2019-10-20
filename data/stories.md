## say goodbye
* goodbye
  - utter_goodbye

## Log Ticket simple
* greet
 - utter_offer_help
* log_ticket
 - action_identify_ticket_attributes
 - utter_ticket_attributes
* affirm
 - action_log_ticket

## Log Ticket change priority
* greet
 - utter_offer_help
* log_ticket
 - action_identify_ticket_attributes
 - utter_ticket_attributes
* deny
 - action_reset_slots
 - ticket_attributes_form
 - form{"name":"ticket_attributes_form"}
 - form{"name":null}
 - action_log_ticket

 ## Log Ticket with priority
* greet
 - utter_offer_help
* log_ticket_with_attributes
* affirm
 - action_log_ticket

## Ticket Status
* greet
 - utter_offer_help
* ticket_status
 - action_get_ticket_status