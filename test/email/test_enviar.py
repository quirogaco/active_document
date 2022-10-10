#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, sys

sys.modules["cgi.parse_qsl"] = None

sys.path.append('D:\gestor_2021_vite')


import logging
from marrow.mailer import Message, Mailer
logging.basicConfig(level=logging.INFO)

mail = Mailer({
        'manager.use': 'futures',
        'transport.use': 'smtp',
        'transport.host': 'smtp.gmail.com',
        'transport.port': '465',
        'transport.tls': 'ssl',
        'transport.username': 'quirogaco@gmail.com',
        'transport.password': 'sreojrjewsjkxnml',
        'transport.max_messages_per_connection': 5
    })
mail.start()

message = Message(
    [('Juan Carlos Rodríguez Ospina', 'quirogaco@gmail.com')], 
    [('Juan Carlos Rodríguez Ospina', 'quirogaco@gmail.com')],
    "This is a test message.", 
    plain="Testing!"
)

mail.send(message)
mail.stop()

"""
from marrow.mailer import Mailer, Message

mailer = Mailer(
    dict(
        transport = 
            dict(
                username = "quirogaco",    
                password = "419803daniel",    
                #use      = 'smtp',
                host     = 'smtp.gmail.com',
                port     = '587'
            )
    )
)
mailer.start()

message = Message(author="quirogaco@gmail.com", to="quirogaco@gmail.com")
message.subject = "Testing Marrow Mailer"
message.plain = "This is a test."
mailer.send(message)

mailer.stop()
"""