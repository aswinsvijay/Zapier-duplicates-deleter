# JTF-CCX-Project
Helper bot for Zapier to delete duplicates.  
Add the bot token to the ```.env``` file before running the code.  
> Note: Use ```git update-index --skip-worktree .env``` to avoid accidental committing of changes to ```.env```  

The bot uses the first line of the message content as primary key. Hence it requires Zapier to be configured to send messages with the primary key in the first line.  
