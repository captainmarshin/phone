# gammu-smsd config file

This is `gammu-smsd` config for Huawei E3131 GSM modem.

Gammu config stores in `/etc/`

```sh
[gammu]                                 # This is modem configuration
port = /dev/ttyUSB0                     # Port of modem. Modem have 3 ports: ttyUSB0, ttyUSB1, ttyUSB2. You need ttyUSB0. If you have more modems, each
                                        # first port in group of three will be the first. For example, for second modem it will be ttyUSB3.
connection = at115200                   # Connection type for Huawei E3131
logfile = /var/log/gammu/gammu.log      # Log file for gammu.
logformat = textall                     # Log setting

[smsd]
Service = files                         # Files setting will be store all SMS on Hard Drive in folders below. You can set db, info in gammu docs.
InboxPath = /var/spool/gammu/inbox/     # Inbox folder
OutboxPath = /var/spool/gammu/outbox/   # Outbox folder
SentSMSPath = /var/spool/gammu/sent/    # Sent folder
ErrorSMSPath = /var/spool/gammu/error/  # Error folder
InboxFormat = unicode                   # Format for incoming SMS
OutboxFormat = unicode                  # Format for outcoming SMS
TransmitFormat = auto                   # The format for transmitting the SMS: auto, unicode, 7bit
debugLevel = 1                          # Log settings
LogFile = /var/log/gammu/smsd.log       # Log file for SMSD. You can leave it for all your configs to get log in one file.
DeliveryReport = sms                    # Delivery report setting
DeliveryReportDelay = 7200              # Delivery report settings
CheckSecurity = 0                       # Check PIN-code. 
PhoneID = first                         # Var for gammu to undesrtand that modem it uses. For second modem set second and etc.

# This is RunOnReceive function, which will launch Receiver script and send message to Telegram bot. Replace user with your system user.
RunOnReceive = /usr/bin/python3 /home/user/phone/receiver.py
```

If you use more modems, you need to create this config for each one.
