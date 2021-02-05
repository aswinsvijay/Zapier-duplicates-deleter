# JTF-CCX-Project
Helper bot for Zapier to delete duplicates.  
Add the bot token to the ```.env_example``` file and rename it to ```.env```.  

By defaut, the bot uses the first line of the message as the primary key.  
This can be changed by sending ```!set-key <pattern>``` to the channel.  
The pattern will be used as a regular expression to find the primary key.  
To reset to default behaviour, use ```!reset-key```.  
