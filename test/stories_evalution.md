## Greet
* greet: Hi
   - utter_offer_help

## Case 1.1: Log ticket with attachment required
* log_ticket: I am getting error while connecting to VPN.
   - action_identify_ticket_attributes
   - utter_ticket_attributes
* affirm: yup
   - utter_attachment_upload
* affirm_attachment: ya sure
   - utter_click_upload
* file_upload: Test File
   - action_log_ticket
   - action_clear_memory
   
## Case 1.2: Log ticket with attachment not required
* log_ticket: I am getting error while connecting to VPN.
   - action_identify_ticket_attributes
   - utter_ticket_attributes
* affirm: ok
   - utter_attachment_upload
* deny_attachment: not now
   - utter_deny_attachment
   - action_log_ticket
   - action_clear_memory
   
## Case 1.3: Log ticket with attachment and Priority Change
* log_ticket: I am getting error while connecting to VPN.
   - action_identify_ticket_attributes
   - utter_ticket_attributes
* change_priority: this is urgent
   - ticket_attributes_form
* affirm_attachment: ya sure
   - utter_click_upload
* file_upload: Test File
   - action_log_ticket
   - action_clear_memory

## Case 1.4: Log ticket without attachment and Priority Change
* log_ticket: I am getting error while connecting to VPN.
   - action_identify_ticket_attributes
   - utter_ticket_attributes
* change_priority: this is urgent
   - ticket_attributes_form
* deny_attachment: not now
   - utter_deny_attachment
   - action_log_ticket
   - action_clear_memory
   
## Case 2.1: Upload document to existing ticket - #TicketID valid
* upload_file_on_ticket: I want to upload a document against my ticket TKT456
 - action_validate_ticket
* file_upload: test file
 - action_file_upload
 - action_clear_memory 
 
## Case 2.2: Upload document to existing ticket - #TicketID invalid
* upload_file_on_ticket:I want to upload a document against my ticket TKT4566
 - action_validate_ticket
* valid_ticketID: my mistake, use TKT456
 - action_validate_ticket
* file_upload: test file
 - action_file_upload
 - action_clear_memory
     
## Log Ticket Form
##* greet: Hello
##    - utter_offer_help
##* log_ticket: My laptop battery is getting drained too quickly.
##    - action_identify_ticket_attributes
##    - utter_ticket_attributes
##* deny: No
##    - action_reset_slots
##    - ticket_attributes_form
##    - action_log_ticket
##    - action_listen 