# Telegram Bot settings

You can config your bot how you want. All settings to bot makes via @BotFather bot in Telegram.

1. Set bot picture
You can download botpic.jpeg from this folder and set Bot picture via @BotFather:
```
/mybots -> Choose your bot -> Edit Bot -> Edit Botpic
```

2. Edit message style
You can edit message, that bot sends, when receive new SMS.

- Open receiver.py file
- Change part of `chat` variable:
```sh
text=<b>☎️: %2B{0}</b>%0A{1} <b>({2})</b>&parse_mode=HTML
```

`<b>☎️: %2B{0}</b>` - This section phone number. `%2B` means + (plus) symbol. `<b>` tag means, that text is bold. `{0}` shows `phone` variable.<br>
`%0A{1} ` - This section shows SMS text. Symbol `%0A` means the new line. `{1}` shows `text` variable.<br>
`<b>({2})</b>` - This section shows sender phone. `{2}` shows `sender` variable, `<b>` tag means, that text is bold.<br>
`&parse_mode=HTML` - This tells Telegram show message with HTML style tags.<br>

You can change message how you want. But if you change `{}` variables, don't forget to change order in `chat` variable in `format` section.

Helpful information:<br>
[Percent-encoding](https://en.wikipedia.org/wiki/Percent-encoding)<br>
[HTML tags](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)<br>
