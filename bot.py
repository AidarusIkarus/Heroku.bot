import telebot
import config
from telebot import types

bot = telebot.TeleBot('5201970475:AAHj_B25VK40N-3gKzdVt9rJs8FnRn6mDk8')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Вас приветствует Ассистент проекта "Робот-тьютор"!")

bot.polling(none_stop=True)


