# helperdroid
*Helper bot for Discord.*

helperdroid is a simple and easy-to-use Discord bot created for the purpose of server administration.

### IMPORTANT NOTE:

Do **NOT** upload your token to any website for any reason or give your token to anyone you do not trust with the utmost certainty. When someone has access to your token, 
they also have access to your bot which means it is possible for them to use your bot with malicious intent.

## Events

Below is a list of all the discord events that helperdroid reacts to.

* On member join:
  * Rules are sent 
    * When a user joins, they are sent a private message consisting of the server rules.
  * New member is greeted
    * When a user joins, they are greeted to the server in the #welcome chat.
    
* On Twitch stream start:
  * Twitch notification is sent
    * When the specified user goes live on Twitch, helperdroid sends a notification to the #twitch-notifications chat with a link to the stream.

## Commands Summary

Below is a list of all the current commands with descriptions.

* help
  * Description: View information on all commands or on a specified commmand.
  * Syntax: ```^help``` or ```^help <command name>```
* rules
  * Description: Display the server rules.
  * Syntax: ```^rules```
