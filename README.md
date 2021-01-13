# JTF-CCX-Project
Helper bot for Zapier to delete duplicates.  
Add the bot token to the ```.env``` file before running the code.  
> Note: Use ```git update-index --skip-worktree .env``` to avoid accidental committing of changes to ```.env```  

By defaut, the bot uses the first line of the message as the primary key.  
This can be changed by sending ```!set-key <pattern>``` to the channel.  
The pattern will be used as a regular expression to find the primary key.  
To reset to default behaviour, use ```!unset-key```.  
