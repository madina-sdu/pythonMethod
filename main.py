import telebot as t
import constants as c

bot = t.TeleBot(c.token)
#bot.send_message(117660721, "some text")

upd = bot.get_updates()


WEBHOOK_HOST = 'https://safe-cliffs-44070.herokuapp.com/'
WEBHOOK_URL_PATH = '/bot'
WEBHOOK_PORT = os.environ.get('PORT',5000)
WEBHOOK_LISTEN = '0.0.0.0'


WEBHOOK_URL_BASE = "https://%s/%s"% (WEBHOOK_HOST,WEBHOOK_URL_PATH)


# last_upd = upd[-1]
# last_updMessage = last_upd.message
# print(last_updMessage)

@server.route("/")
def webhook():
    bot.remove_webhook()
    # Если вы будете использовать хостинг или сервис без https
    # то вам необходимо создать сертификат и
    # добавить параметр certificate=open('ваш сертификат.pem')
    return "%s" %bot.set_webhook(url=WEBHOOK_URL_BASE), 200

@server.route("/remove")
def remove_hook():
    bot.remove_webhook()
    return "Webhook has been removed"

@bot.message_handler(commands=["help"])
def handle_text(message):
    bot.send_message(message.chat.id, "Я бот, который поможет тебе узнать все о нашей школе!")

@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = t.types.ReplyKeyboardMarkup(True)
    user_markup.row('/start', '/stop')
    user_markup.row('About', 'Courses', 'Location')
    user_markup.row('Contacts', 'Website')
    bot.send_message(message.from_user.id, "Welcome!", reply_markup = user_markup)

@bot.message_handler(commands=["stop"])
def handle_start(message):
    hide_markup = t.types.ReplyKeyboardHide()
    bot.send_message(message.from_user.id, "Bye! We're waiting for u =)", reply_markup = hide_markup)
@bot.message_handler(content_types=["commands"])
def handle_command(message):
    print("Пришла команда")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = "Привет! Как дела?"
    if message.text == "Привет":
        bot.send_message(message.chat.id, """ \r 
        <b>Bold Text</b>
        <i>Italic Text</i>
        <code>Inline fixed-width</code>
        <a href="google.com">google.com</a>
        
        """, parse_mode="HTML")
    elif message.text == "Location":
        print("zawel")
        # bot.send_chat_action(message.from_user.id, "finding location")
        bot.send_location(message.from_user.id, 43.2291144, 76.9506943)
    elif message.text == "About":
         bot.send_message(message.chat.id, """ \r 
        <b>Method Coding School</b> \n
<code>Школа программирования Метод
Мы крутые чуваки! Записывайтесь кароч!</code>
        
        """, parse_mode="HTML")
    elif message.text == "Website":
        bot.send_message(message.chat.id, """ \r 
        <a href="method.kz">method.kz</a>
        """, parse_mode="HTML")
    elif message.text == "Contacts":
        bot.send_message(message.chat.id, """ \r 
        <b>Telephone: </b> 8-777-77-77
<b>Director: </b> Nurbolat Kusmagul
<b>Days: </b> Mn - Sn
<b>Hours: </b> 09:00 - 21:00
        """, parse_mode="HTML")
    elif message.text == "Courses":
        bot.send_message(message.chat.id, """ \r 
        <i>Soon here will be all information about our courses</i>
        """, parse_mode="HTML")

@bot.message_handler(content_types=["document"])
def handle_command(message):
    print("Пришел документ")

@bot.message_handler(content_types=["sticker"])
def handle_command(message):
    print("Пришел стикер")

@bot.message_handler(content_types=["audio"])
def handle_command(message):
    print("Пришло аудио")

@bot.message_handler(content_types=["photo"])
def handle_command(message):
    print("Пришло фото")

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
webhook()