## greet
* greet
  - utter_offer_help
  
## say goodbye
* goodbye
  - utter_goodbye

## thank from user
* thank
  - utter_welcome_message
  
## Case 1.1: Log ticket with attachment required 
* log_ticket
 - action_identify_ticket_attributes
 - utter_ticket_attributes
* affirm
 - utter_attachment_upload
* affirm OR affirm_attachment
 - utter_click_upload
* file_upload
 - action_log_ticket
 - action_clear_memory

## Case 1.2: Log ticket with attachment not required 
* log_ticket
 - action_identify_ticket_attributes
 - utter_ticket_attributes
* affirm
 - utter_attachment_upload
* deny OR deny_attachment
 - utter_deny_attachment
 - action_log_ticket
 - action_clear_memory
 
## Case 1.3: Log ticket with attachment and Priority Change
* log_ticket
 - action_identify_ticket_attributes
 - utter_ticket_attributes
* change_priority
 - ticket_attributes_form
 - form{"name":"ticket_attributes_form"}
 - form{"name":null}
* affirm OR affirm_attachment
 - utter_click_upload
* file_upload
 - action_log_ticket
 - action_clear_memory
 
## Case 1.4: Log ticket without attachment and Priority Change
* log_ticket
 - action_identify_ticket_attributes
 - utter_ticket_attributes
* change_priority
 - ticket_attributes_form
 - form{"name":"ticket_attributes_form"}
 - form{"name":null}
* deny OR deny_attachment
 - utter_deny_attachment
 - action_log_ticket
 - action_clear_memory 
 
## Case 2.1: Upload document to existing ticket - #TicketID valid
* upload_file_on_ticket
 - action_validate_ticket
* file_upload
 - action_file_upload
 - action_clear_memory 
 
## Case 2.2: Upload document to existing ticket - #TicketID invalid
* upload_file_on_ticket
 - action_validate_ticket
* valid_ticketID
 - action_validate_ticket
* file_upload
 - action_file_upload
 - action_clear_memory
 
 