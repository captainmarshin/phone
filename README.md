![Phone logo](https://github.com/captainmarshin/phone/blob/main/PREVIEW.png?raw=true)

# Phone
Receive SMS from Huawei E3131 GSM modem via Gammu to Telegram bot.

## Table of Contents:
- [Phone](#phone)
  * [Requariements](#requariements)
  * [Installation](#installation)
  * [Config Gammu](#config-gammu)
  * [Config Telegram Bot](#config-telegram-bot)
  * [Config Receiver.py](#config-receiverpy)
- [Create systemctl for gammu-smsd](#create-systemctl-for-gammu-smsd)
  * [Montoring](#montoring)


## Requariements
* Ubuntu 22.04
* Huawei E3131 GSM Modem (+ patch to unlock SIM)
* usbmodeswitch
* Gammu
* gammu-smsd
* Python 3.10.6 +
* Telegram

## Installation

1. Insert SIM in modem, check that modem is connected and availabe in system
```bash
lsusb
```
Huawei Huawei Technologies Co., Ltd output means, that modem is connected to PC.

2. Switch modem mode with usbmodeswitch

```bash
sudo usb_modeswitch -v 12d1 -p 14fe -M '55534243123456780000000000000011062000000100000000000000000000'
```
12d1 and 14fe - it's a ID of modem from lsusb. It can be different.

More info and guide:
https://askubuntu.com/a/1146339

3. Install Gammu and gammu-smsd

Instruction from here:
https://github.com/playsms/book-playsms/blob/master/book-contents/en/Installation/Gateway-Installation/Gammu/Gammu-installation-via-apt-get-on-Ubuntu.md

- Make sure you have root access
```bash
sudo su -
```

- Install Gammu via apt-get
```bash
apt-get install gammu gammu-smsd
```

- Create required directories
```bash
mkdir -p /var/log/gammu /var/spool/gammu/{inbox,outbox,sent,error}
```
Note: The directory names are case-sensitive

- Setup Gammu spool directories owner and permission
! In this example your webserver's user and group is www-data
```bash
chown www-data:www-data -R /var/spool/gammu/*
```

You can also set files and folders permission to world-writable
```bash
chmod 777 -R /var/spool/gammu/*
```

## Config Gammu

You need to create config for each connected modem.

Use standart gammu-smsd config as first, create another configs in /etc/

Edit first config
```bash
nano /etc/gammu-smsdrc
```

Config description:
```bash
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

If you have more modems:

* Change port - you need first port from 3 port group for Huawei E3131
* Change PhoneID - you can name it like you want. For more user friendly I use first for first modem, second for second and so on.
* Change RunOnReceive - copy receiver.py script with new name (for ex.: receiver2.py) and change phone var and so on.

## Config Telegram Bot

1. Go to @BotFather and run /newbot
2. Choose name for bot (for example: Phone)
3. Choose username for bot (anyname with bot at the end)
4. Copy Bot Token.

You can add picture, description and etc. Examples in bot folder.

5. Go to you bot, press Start

6. Open browser and run this API request:

Replace *YOUR_TOKEN* with Bot Token from @BotFather

```bash
https://api.telegram.org/bot*YOUR_TOKEN*/getUpdates
```

7. From URL output get chat_id number.
This is your Telegram ID.

## Config Receiver.py

1. Replace phone var with your modem phone number.
This variable contains your modem phone number and uses for show you, from which modem you receive SMS. You can change it to any text you want.
If you use number - type it without + (plus). 
If you use text name - remove %2B from chat url. (%2B it's a + (plus) in Percent-encoding https://en.wikipedia.org/wiki/Percent-encoding)

2. Edit chat variable:

```bash
chat = "https://api.telegram.org/bot*YOUR_TOKEN*/sendMessage?chat_id=*YOUR_ID*&text=<b>☎️: %2B{0}</b>%0A{1} <b>({2})</b>&parse_mode=HTML".format(phone, text, sender)
```

*YOUR_TOKEN* - replace this with your Bot Token from @BotFather
*YOUR_ID* - replace this with your Telegram ID

If you use more modems, copy receiver.py with new name (for example: receiver2.py and so on) and change only phone number var.

# Create systemctl for gammu-smsd

1. Create gammu-modem-1.service file in /etc/systemd/system/
```bash
nano /etc/systemd/system/gammu-modem-1.service
```

2. Edit created config file
```bash
[Unit]
Description=Gammu Modem 1                     # Description for service
serviceAfter=network.target                   # Start after network service
StartLimitIntervalSec=0                       # Limit interval for start service

[Service]
Type=simple                                   # Type of service
Restart=always                                # Always restart if service goes down
RestartSec=1                                  # Seconds to restart after service down
User=user                                     # System username
ExecStart=gammu-smsd -c /etc/gammu-modem-1    # Start gammu-smsd with modem config

[Install]
WantedBy=multi-user.target
```

* Change Description to your service name (or leave as it is)
* Change User to your system username
* Change ExecStart to your Gammu config (or leave as it is, if you config name the same)

If you have more modems, create .service file for each modem and replace Gammu config with config name for this modem.
For example, if you have to modems, you need gammu-modem-1.service and gammu-modem-1.service files with /etc/gammu-modem-1 and /etc/gammu-modem-2 configs in it.

3. Launch system services
```bash
systemctl start gammu-modem-1.service
```
If you have more modems, run systemctl start for each one.

4. Check, that service is working
```bash
systemctl status gammu-modem-1.service
```

Output:
```bash
● gammu-modem-1.service - Modem 1 Reciever (Gammu)
     Loaded: loaded (/etc/systemd/system/gammu-modem-1.service; enabled; vendor preset: enabled)
     Active: active (running) since Sat 2022-12-24 10:29:26 MSK; 4 days ago
   Main PID: 3883959 (gammu-smsd)
      Tasks: 1 (limit: 4534)
     Memory: 3.1M
        CPU: 55.233s
     CGroup: /system.slice/gammu-modem-1.service
             └─3883959 gammu-smsd -c /etc/gammu-smsdrc

Dec 24 10:29:26 user systemd[1]: Started Modem 1 Receiver (Gammu).
```

## Montoring

1. Check services running
```bash
systemctl status gammu-modem-1.service
```

2. Restart services
```bash
systemctl restart gammu-modem-1.service
```

3. Check gammu log
```bash
tail -f /var/log/gammu/smsd.log
```
