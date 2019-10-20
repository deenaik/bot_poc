## say goodbye
* goodbye
  - utter_goodbye

## Log Ticket simple
* greet
 - utter_offer_help
* log_ticket
 - action_identify_ticket_attributes
## - utter_ticket_attributes_confirmation
* affirm
 - action_log_ticket

## Log Ticket change priority
* greet
 - utter_offer_help
* log_ticket
 - action_identify_ticket_attributes
 - utter_ticket_attributes_confirmation
* deny
 - action_select_priority
 - action_log_ticket

## Log Ticket with priority
* greet
 - utter_offer_help
* log_ticket
 - action_identify_ticket_attributes
 - action_log_ticket

## Ticket Status
* greet
 - utter_offer_help
* ticket_status
 - action_get_ticket_status
