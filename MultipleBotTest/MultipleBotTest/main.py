from flask import Flask, request
import telebot
from telebot import types
import os


app = Flask(__name__)
TOKEN = os.environ.get("TOKEN")  #os - server request module. environ - dict
bot = telebot.TeleBot(TOKEN)  #connect to telegram


@bot.message_handler(commands=["start"])
def message_start(message):
    bot.send_message(message.chat.id, "Hello, user!\nPrint /help for info")

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Help")
    markup.add(item1)
    bot.send_message(message.chat.id, "Print name of operation through '/' then 'space' 1st number 'space' 2nd number\n"
                                      "Operations: /add , /sub, /mul, /div", reply_markup=markup)

# @bot.message_handler(commands=["help"])
# def message_table(message):
#     bot.send_message(message.chat.id, "Print name of operation through '/' then 'space' 1st number 'space' 2nd number\n"
#                                       "Operations: /add , /sub, /mul, /div")


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
