## Log ticket Scenario 1
* greet
  - utter_offer_help
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

## Log Ticket Scenario 2
* greet
  - utter_offer_help
* log_ticket
 - action_identify_ticket_attributes
 - utter_ticket_attributes
* affirm
 - utter_attachment_upload
* deny OR deny_attachment
 - utter_deny_attachment
 - action_log_ticket
 - action_clear_memory


## Log Ticket Scenario 3
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
 - utter_attachment_upload
* affirm OR affirm_attachment
 - utter_click_upload
* file_upload
 - action_log_ticket
 - action_clear_memory

 ## Log Ticket Scenario 4
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
 - utter_attachment_upload
* deny OR deny_attachment
 - action_log_ticket
 - action_clear_memory