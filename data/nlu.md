## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- nope
- modify the priority
- just change the priority
- i don't agree with this priority

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:log_ticket
- I am getting error while connecting to VPN.
- I am not able to connect to demo application from office desktop.
- My laptop battery is getting drained too quickly.
- Need to increase machine RAM for installing SOLR setup.
- My laptop screen is showing black spots.
- My laptop mouse pad giving trouble.
- I need LDAP Sever on AWS for automation run.
- I need oracle client installed on my laptop.
- Can anyone look into Sahi Pro installation for my laptop?
- I need access to coursera portal for AI related courses.
- I require youtube access for watching share point tutorials.

## intent:affirm_attachment
- yes now
- yes required
- required
- needed it
- it is relevant
- sure
- ya why not
- yes please
- ya sure

## intent:deny_attachment
- not now
- not required
- forget it
- not needed
- not relevant
- maybe later
- later

## intent:affirm
- yes
- correct
- affirmative that is fine yes
- sure, please go ahead
- that is good
- yes sir
- affirmative that is good yep
- ya
- fine
- ok
- agreed
- agreed yep
- right
- yup
- go ahead
- done
- ok done
- affirmative please
- yep
- sounds good
- sounds good right
- yes sir please
- yes sounds good
- yep that is good
- i am ok with that
- yep that is correct
- yes right
- yes correct
- yes you understood me i am ok with that
- correct sir thank you
- i am ok with that
- affirmative right
- agreed yep
- indeed
- of course
- that sounds good

## intent:log_ticket_with_attributes
- My laptop is not working, log a [critical priority](priority) [hardware issue](category) ticket
- My laptop is not working, log a [critical](priority) [hardware issue](category) ticket

## intent:get_priority
- [Critical Priority](priority)
- [Critical](priority)
- [High](priority)
- [Medium](priority)
- [Low](priority)
- [critical priority](priority)
- [critical](priority)
- [high](priority)
- [medium](priority)
- [low](priority)
- Log a [critical issue](priority)
- Log a [high issue](priority)
- Log a [medium issue](priority)
- Log a [low issue](priority)
- [High Priority](priority)
- [Medium Priority](priority)
- [Low Priority](priority)
- no, this issue is a [showstopper](priority) for me, my work is stuck
- no, this issue is a [showstopper](priority)
- log a [critical issue](priority)
- I need this to be logged as a [critical issue](priority)
- change priority to [critical](priority)
- I need it [asap](priority)
- this is [urgent](priority)
- this is [showstopper](priority)
- log it as [medium](priority)
- make it [medium](priority)
- change priority to [medium](priority)
- this can be considered as [medium](priority)

## synonym:critical
- urgent
- showstopper
- asap

## intent:file_upload
- Test File
- Attachment

## intent:thank
- Thanks, that was great help !!
- Thanks that was helpful !!!
- That was indeed helpful
- You are a blessing
- thnx
- thank u
- thank you
- thanks
- Thank you
- Thanks
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks a ton
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you
- thanks!
- thanks that was great help

## intent:get_ticketID
- [TKT456](ticketID)
- [TKT234](ticketID)
- [TKT123](ticketID)
- [TKT789](ticketID)
- [TKT677](ticketID)
- [TKT777](ticketID)
- [TKT546](ticketID)
- [TKT789](ticketID)
- [TKT4566](ticketID)
- I want to upload a document against my ticket [TKT456]
- can you upload a file for [TKT456](ticketID)
- i need to upload a doc against [TKT123](ticketID)
- hey, attach a document against [TKT789](ticketID)
- can you attach a doc on [TKT677](ticketID)
- can you load a doc on [TKT234](ticketID)
- i need to load a doc against [TKT546](ticketID)
- please upload a doc file against [TKT789](ticketID)

## intent:valid_ticketID
- my bad, the id is [TKT456](ticketID)
- my mistake, use [TKT456](ticketID)
- ohh, its [TKT456](ticketID)
- ok try [TKT456](ticketID)

## intent:get_ticket_status
- What is the current status of my ticket [TKT456](ticketID)
- get me the status of [TKT123](ticketID)
- show me the current status of [TKT456](ticketID)
- i need status of [TKT234](ticketID)
- gimme status of [TKT456](ticketID)
- find the status of [TKT678](ticketID)
- can you help me with the status of [TKT675](ticketID)
- get me status of [TKT555](ticketID)
- help me status of [TKT234](ticketID)
- track the status of [TKT789](ticketID)
- what is the progress on [TKT345](ticketID)
- report the progress of [TKT789](ticketID)
- gimme status of [TKT4566](ticketID)


## intent:file_upload_json
- { file: [FPC96EY3V](file), text: [''](file_text) }
- { file: [FPC96EY3V](file), text: ['Attachment'](file_text) }
- { file: [FPC96EY3V](file), text: ['Sample File'](file_text) }
- { file: [FPC96EY3V](file), text: ['Screenshot'](file_text) }