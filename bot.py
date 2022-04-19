import telebot
import config
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup
keyboard = ReplyKeyboardMarkup(True)
keyboard.row('/start', '/info')
keyboard.row('/change_mode')

bot = telebot.TeleBot('5201970475:AAHj_B25VK40N-3gKzdVt9rJs8FnRn6mDk8')
@bot.message_handler(commands=['info'])
def info_func (message):
    inline=InlineKeyboardMarkup()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Вас приветствует бот проекта "Робот-тьютор"! Здесь вы можете выбрать режим игры:')
@bot.message_handler(commands=['change_mod'])
def change_mod(message):
    bot.send_message(message.chat.id, 'lorem')

bot.polling(none_stop=True)


