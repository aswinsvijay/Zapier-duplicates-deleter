# JTF-CCX-Project
Helper bot for Zapier to delete duplicates.  
Add the bot token to the ```.env``` file before running the code.  
The bot uses email present in the message as primary key to find duplicates and delete them. It is required that there should be at least one whitespace before and after the email, and the ```@``` symbol must not be present anywhere in the message other than in the email.  
