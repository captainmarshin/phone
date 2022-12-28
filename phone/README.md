# receiver.py

This is script, that will be launch in RunOnReceive gammu-smsd option. You can modify script how you want.
If you use more modems, don't forget to copy this script, rename it and set in second Gammu config.

## Change `phone` number
```python
phone = "70000000000"
```
This variable shows you modem phone number. You can type number or text. If you use number, type it without + (plus). If you use text, remove `%2B` from chat variable.

## Change `chat` variable
```python
chat = "https://api.telegram.org/bot__/sendMessage?chat_id=__&text=<b>☎️: %2B{0}</b>%0A{1} <b>({2})</b>&parse_mode=HTML".format(phone, text, sender)
```
Replace `__` in `bot` with you Telegram Bot Token. Replace `__` in `chat_id` with your Telegram ID.

## Customize bot message
```python
<b>☎️: %2B{0}</b>%0A{1} <b>({2})</b>&parse_mode=HTML
```

`<b>☎️: %2B{0}</b>` - This section phone number. `%2B` means + (plus) symbol. `<b>` tag means, that text is bold. `{0}` shows `phone` variable.<br>
`%0A{1} ` - This section shows SMS text. Symbol `%0A` means the new line. `{1}` shows `text` variable.<br>
`<b>({2})</b>` - This section shows sender phone. `{2}` shows `sender` variable, `<b>` tag means, that text is bold.<br>
`&parse_mode=HTML` - This tells Telegram show message with HTML style tags.<br>

You can change message how you want. But if you change `{}` variables, don't forget to change order in `chat` variable in `format` section.
