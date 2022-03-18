import telebot

bot = telebot.TeleBot('5201970475:AAHj_B25VK40N-3gKzdVt9rJs8FnRn6mDk8')
@bot.message_handler(commands=['start'])
def info(message):
    bot.send_message(message.chat.id, 'Это мой бот!')

bot.polling(none_stop=True)


