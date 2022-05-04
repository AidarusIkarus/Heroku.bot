import config
import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InlineKeyboardButton
import paho.mqtt.client as mqtt
hostname='mqtt.pi40.ru'

bot = telebot.TeleBot('5201970475:AAHj_B25VK40N-3gKzdVt9rJs8FnRn6mDk8')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Вас приветствует илья Ассистент проекта Робот-тьютор! Выберите что вам надо:')
    inline=ReplyKeyboardMarkup()
    b1 = InlineKeyboardButton('Выбрать режим игры', callback_data='button1')
    inline.add(b1)
    b2 = InlineKeyboardButton('2', callback_data='button2')
    inline.add(b2)
    b3 = InlineKeyboardButton('3', callback_data='button3')
    inline.add(b3)
    b4 = InlineKeyboardButton('4', callback_data='button4')
    inline.add(b4)

bot.polling(none_stop=True)
