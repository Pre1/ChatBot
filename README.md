### A Chat bot for testing
#### Also it'll serve coffee :)

##### Commands: 

	- `/cal`: eg: `/cal 1+23+1` no spaces between math operations.
	- `/today`: to show today's date (hey Mr Obvious)
	- `/post`: post (number of messages) (wait time betwreen each msg in sec)
					(Channel ID: `id=<ch_id>` or `-` to post the default channel)
					(your messgge)

		eg: `/post 2 3 - test`
		=> this will post 2 msgs, wait 3 sec between
		each msg, it'll be posted in the current channel 
		and the message will be `test`. 

		eg: `/post 2 3 id=123 test`
		=> same thing as the above but it'll be posted
		to a channel with ID of `123`


THe bot works on the Chatr proj by default: https://github.com/Pre1/Chatr2.0-UI
