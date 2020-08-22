# MailingPythonProgram

As there're some problems in sending an email to multiple participants in Gmail; like personalizing or security.
This program will help automating the whole process so you don't need to copy and paste emails anymore!

The process is simple:
- First, you need to prepare a csv (comma seperated values) file for all your participants or receivers. Mainly, you must have an "Email" collomn (That's required for obvios reasons) and you can add other values as you wish if you want to use them (see receiversDataSample.csv).
  Note that if your data is on Google Forms you can just download it as scv and work with it right away.
- Next, you need to prepare an HTML file for your email body. It needs to be in html form to help formatting the email as you want. (see mailBodySample.html) 
  Note that you can add place holders for the key you want as %%key%% and the program will replace this with the value corresponding to each participant.
- Next, make sure the sender account is set for this kind of process as it needs the 2-step verification key to be inactive and Less Secure Apps to be ON. 
  Note that any files need to be at the same directory as the program or providing the full path otherwise.
- Finally, run the program and provide the required information like sender authentications and email subject etc.

That's it! Now you can go ahead and send your mail for as many as you want and with your custom formatting.
Hope it was useful!
