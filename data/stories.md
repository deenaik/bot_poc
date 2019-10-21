## greet
* greet
  - utter_offer_help
  
## say goodbye
* goodbye
  - utter_goodbye
 
 ## say thanks
* affirm_good_work 
 - utter_welcome_message

## Log Ticket simple
* log_ticket
 - action_identify_ticket_attributes
 - utter_ticket_attributes
* affirm
 - action_log_ticket
 - utter_attachment_upload
* affirm_attachment
 - utter_click_upload
 - utter_upload_successful
 
 ## Log Ticket simple deny attachment
* log_ticket
 - action_identify_ticket_attributes
 - utter_ticket_attributes
* affirm
 - action_log_ticket
 - utter_attachment_upload
* deny_attachment
 - utter_deny_attachment
  
## Log Ticket change priority
* log_ticket
 - action_identify_ticket_attributes
 - utter_ticket_attributes
* deny
 - action_reset_slots
 - ticket_attributes_form
 - form{"name":"ticket_attributes_form"}
 - form{"name":null}
 - action_log_ticket
 - utter_attachment_upload

 ## Log Ticket with priority
* log_ticket_with_attributes
* affirm
 - action_log_ticket
 - utter_attachment_upload
 

## Ticket Status
* ticket_status
 - action_get_ticket_status