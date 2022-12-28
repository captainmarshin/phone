# Receive messages from GSM modem via Gammu to Telegram
# https://github.com/captainmarshin/phone/
#
#!/usr/bin/env python

import os
import sys
import requests

numparts = int(os.environ["DECODED_PARTS"])
phone = "70000000000"
sender = str(os.environ["SMS_1_NUMBER"])

text = ""

if numparts == 0:
    text = os.environ["SMS_1_TEXT"]
else:
    for i in range(1, numparts + 1):
        varname = "DECODED_%d_TEXT" % i
        if varname in os.environ:
            text = text + os.environ[varname]

headers = { "Accept": "application/json", "Content-Type": "application/json" }
chat = "https://api.telegram.org/bot__/sendMessage?chat_id=__&text=<b>☎️: %2B{0}</b>%0A{1} <b>({2})</b>&parse_mode=HTML".format(phone, text, sender)
notify = requests.get(chat, headers = headers)