from flask import Flask, request
import telebot
import os


app = Flask(__name__)
TOKEN = os.environ.get("TOKEN")  #os - server request module. environ - dict
bot = telebot.TeleBot(TOKEN)  #connect to telegram


@bot.message_handler(commands=["start", "help"])
def message_start(message):
    bot.send_message(message.chat.id, "Hello, user! Input expression")


@bot.message_handler(content_types=['text'])
def message_text(message):
    if message.text.lower().startswith('слава нації'):
        bot.send_message(message.chat.id, 'Смерть ворогам!')


@bot.message_handler(func=lambda x: x.text.lower().startswith("python"))
def message_text(message):

    bot.send_message(message.chat.id, "Python")


@app.route("/" + TOKEN, methods=["POST"])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot", 200

@app.route("/")
def main():
    bot.remove_webhook()
    bot.set_webhook(url="https://multipletestbot.herokuapp.com/" + TOKEN)  #url - adress of app(Heroku)
    return "Python Telegram Bot", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
