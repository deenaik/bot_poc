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
  - action_log_message
  - action_identify_ticket_attributes
  - utter_ticket_attributes
* affirm
  - utter_attachment_upload
* affirm OR affirm_attachment
  - action_clear_file
  - ticket_file_form
  - form{"name":"ticket_file_form"}
  - form{"name":null}
  - action_log_ticket
  - action_clear_memory

## Case 1.2: Log ticket with attachment not required 
* log_ticket
  - action_log_message
  - action_identify_ticket_attributes
  - utter_ticket_attributes
* affirm
  - utter_attachment_upload
* deny OR deny_attachment
  - action_log_ticket
  - action_clear_memory
 
## Case 1.3: Log ticket with attachment and Priority Change
* log_ticket
  - action_log_message
  - action_identify_ticket_attributes
  - utter_ticket_attributes
* deny
  - action_clear_priority
  - ticket_attributes_form
  - form{"name":"ticket_attributes_form"}
  - form{"name":null}
  - utter_attachment_upload
* affirm OR affirm_attachment
  - action_clear_file
  - ticket_file_form
  - form{"name":"ticket_file_form"}
  - form{"name":null}
  - action_log_ticket
  - action_clear_memory
 
## Case 1.4: Log ticket without attachment and Priority Change
* log_ticket
  - action_log_message
  - action_identify_ticket_attributes
  - utter_ticket_attributes
* deny
  - action_clear_priority
  - ticket_attributes_form
  - form{"name":"ticket_attributes_form"}
  - form{"name":null}
  - utter_attachment_upload
* deny OR deny_attachment
  - action_log_ticket
  - action_clear_memory
  
## Case 3.1: Get ticket status - #Ticketid valid  
* get_ticket_status
  - action_log_message
  - action_validate_ticket_for_status
  - action_get_ticket_status
  - action_clear_memory