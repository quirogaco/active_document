#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, sys

sys.modules["cgi.parse_qsl"] = None

sys.path.append('D:\gestor_2021_vite')

import smtplib

gmail_user = 'quirogaco@gmail.com'
gmail_password = 'sreojrjewsjkxnml'

sent_from = gmail_user
to = ['quirogaco@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, whats up You'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print( 'Email sent!')
except Exception as e:
    print('Something went wrong...', str(e))