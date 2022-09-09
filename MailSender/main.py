import smtplib
import ssl
from email.message import EmailMessage
from password import password1

email_sender = 'email_of_the_sender'
email_password = password1

email_receiver = 'email_of_the_receiver'

subject = 'This is a Python Mail'
body = """
     This is a 
     Multiline 
     Mail Message
     From Thara
"""

em = EmailMessage()
# It is the base class for the email object model.
# EmailMessage provides the core functionality
# for setting and querying header fields, for accessing message bodies,
# and for creating or modifying structured messages

em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
# create_default_context() . The default SSL context is good for a client connecting to a server.

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
