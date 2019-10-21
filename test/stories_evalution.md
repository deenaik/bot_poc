## Simple Log Ticket
* greet: Hi
   - utter_offer_help
* log_ticket: I am getting error while connecting to VPN.
   - action_identify_ticket_attributes
   - utter_ticket_attributes
* affirm: yup
   - action_log_ticket

## Log Ticket Form
* greet: Hello
    - utter_offer_help
* log_ticket: My laptop battery is getting drained too quickly.
    - action_identify_ticket_attributes
    - utter_ticket_attributes
* deny: No
    - action_reset_slots
    - ticket_attributes_form
    - action_log_ticket
    - action_listen 