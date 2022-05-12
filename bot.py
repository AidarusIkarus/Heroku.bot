import config
import random
import time
from telebot import *
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup
import paho.mqtt.client as mqtt


hostname='mqtt.pi40.ru'
port=1883
username='aidar'
password='aidar1234'
topic='aidar/tg'
client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(hostname, port, 60)

spisok_zagadok = ['Бурый, косолапый по лесу бредёт.\nЛюбит «одолжить» он у лесных пчёл мёд.',
                  'Рыжая плутовка,\nХитрая, да ловкая,\nВ сарай попала, \nКур пересчитала.',
                  'Кто любить не устает,\nПироги для нас печет,\nВкусные оладушки?\nЭто наша...',
                  'Я у мамы не один,\nУ неё ещё есть сын,\nРядом с ним я маловат,\nДля меня он — старший...',
                  'Он трудился не от скуки,\nУ него в мозолях руки,\nА теперь он стар и сед —Мой родной, любимый...',
                  'Кто же с маминой сестрой\nПриезжает к нам порой?\nНа меня с улыбкой глядя,\nЗдравствуй! — говорит мне...',
                  'Заплелись густые травы,\nЗакудрявились луга,\nДа и сам я весь кудрявый,\nДаже завитком рога.',
                  'У него огромный рот,\nОн зовется …',
                  'Хожу в пушистой шубе,\nЖиву в густом лесу.\nВ дупле на старом дубе\nОрешки я грызу.',
                  'С ветки на ветку, быстрый, как мяч,\nСкачет по лесу рыжий циркач.\nВот на лету он шишку сорвал,\nПрыгнул на ствол и в дупло убежал.',
                  'Кто по ёлкам ловко скачет\nИ взлетает на дубы?\nКто в дупле орехи прячет,\nСушит на зиму грибы?',
                  'По деревьям скок-скок,\nА орешки щёлк-щёлк.',
                  'Кто милее всех на свете?\nКого любят очень дети?\nНа вопрос отвечу прямо:\nВсех милее наша...',
                  'Кто нежнее всех на свете?\nКто готовит нам обед?\nИ кого так любят дети?\nИ кого прекрасней нет?\nКто читает на ночь книжки?\nРазгребая горы хлама,\nНе ругает нас с братишкой.\nКто же это? Наша...',
                  'В школе сложная программа,\nНо всегда поможет...']

answers = ['Медведь','Лиса','Бабушка','Брат','Дед','Дядя','Баран','Бегемот','Белка','Белка','Белка','Белка','Мама','Мама','Мама']

eatable = ['Абрикос', 'Апельсин', 'Арбуз', 'Банан', 'Виноград', 'Гранат', 'Груша', 'Киви', 'Ананас', 'Лимон', 'Персик', 'Яблоко', 'Мандарин',
           'Огурец', 'Помидор', 'Лук', 'Чеснок', 'Картошка', 'Кабачок', 'Баклажан', 'Перец', 'Капуста', 'Морковь', 'Свекла', 'Грибы', 'Кукуруза',
           'Репа', 'Горошек', 'Редис', 'Редька', 'Брокколи', 'Тыква', 'Укроп', 'Хлеб', 'Суп', 'Салат', 'Каша', 'Батон', 'Печенье', 'Шоколад', 'Сметана',
           'Молоко', 'Сок', 'Компот', 'Вода', 'Кофе', 'Мороженое', 'Бургер', 'Макароны', 'Сосиска', 'Варенье', 'Блины', 'Пирожное',
           'Картофельное пюре', 'Соус', 'Гречка', 'Плов', 'Клубника', 'Смородина', 'Земляника']

uneatable = ['Мяч', 'Книга', 'Рука', 'Плюшевый мишка', 'Карандаш', 'Стул', 'Стол', 'Поезд', 'Машина', 'Диван', 'Шкаф', 'Дверь', 'Стена', 'Окно', 'Дерево',
             'Бумага', 'Ножницы', 'Камень', 'Бутылка', 'Колодец', 'Снеговик', 'Черепаха', 'Платье', 'Тарелка', 'Ложка', 'Вилка', 'Нож', 'Салфетка', 'Маска',
             'Сумка', 'Рюкзак', 'Шляпа', 'Штаны', 'Брюки', 'Краски', 'Мыло', 'Кисточка', 'Свечка', 'Колесо', 'Руль', 'Ракета', 'Телефон', 'Телевизор', 'Песок',
             'Куртка', 'Молоток', 'Ключи', 'Кирпич', 'Доска', 'Дом', 'Кровать', 'Палка', 'Лампочка', 'Трактор', 'Сиденье', 'Часы', 'Карта', 'Подоконник',
             'Компьютер', 'Ручка', 'Балкон', 'Ваза', 'Миска', 'Пульт', 'Духи', 'Табуретка']
eatgame = [eatable, uneatable]
pictures = ['абрикос.jpg', 'ананас.jpg', 'арбуз.jpg', 'банан.jpg', 'вилка.jpg', 'горошек.jpg', 'гречка.jpg', 'грибы.png', 'груша.jpg', 'дверь.jpg', 'дом.jpg',
            'ежевика.jpg', 'земляника.jpg', 'кабачок.jpg', 'капуста.jpg', 'картошка.jpg', 'клубника.jpg', 'лимон.jpg', 'ложка.jpg', 'лук.jpg', 'макароны.jpg',
            'малина.jpg', 'мандарин.jpg', 'морковь.jpg', 'огурец.jpg', 'помидор.jpg', 'редис.jpg', 'репа.jpg', 'свекла.jpg', 'сосиска.jpg', 'стол.jpg',
            'стул.jpg', 'тарелка.jpg', 'тыква.jpg', 'чеснок.jpg', 'шоколад.jpg', 'яблоко.jpg']

p_answers = ['Абрикос', 'Ананас', 'Арбуз', 'Банан', 'Вилка', 'Горошек', 'Гречка', 'Грибы', 'Груша', 'Дверь', 'Дом', 'Ежевика', 'Земляника', 'Кабачок', 'Капуста',
             'Картошка', 'Клубника', 'Лимон', 'Ложка', 'Лук', 'Макароны', 'Малина', 'Мандарин', 'Морковь', 'Огурец', 'Помидор', 'Редис', 'Репа', 'Свекла', 'Сосиска',
             'Стол', 'Стул', 'Тарелка', 'Тыква', 'Чеснок', 'Шоколад', 'Яблоко']


def change_zag():
    number = random.randint(0, len(spisok_zagadok) - 1)
    zagadka = spisok_zagadok[number]
    zagadka_used = []

    if zagadka not in zagadka_used:
        word = zagadka
        answer = answers[number]
        spisok_zagadok.remove(spisok_zagadok[number])
        zagadka_used.append(word)
        return zagadka, answer
    else:
        pass
def f_eatgame():
    category = random.choice(eatgame)
    thing = random.choice(category)
    if category == eatable:
        return 'Съедобное 🍽', thing
    else:
        return 'Несъедобное 🚫', thing

def f_pictures():
    global photo
    pct = random.choice(pictures)
    photo = open(pct, 'rb')
    return photo , p_answers[pictures.index(pct)]

sticker_gb='CAACAgIAAxkBAAMfYnVLxK9dvz__EWVuKgRB6mQdB_sAAvIZAAKsJalL4vko8zV6PikkBA'
zagad,otvet=change_zag()

bot = telebot.TeleBot('5364331161:AAFiGJS0IGq81InKVY1vtlNbs7PRkRn4b9o')

flag=False
@bot.message_handler(commands=['start'])
def start(message):
    global flag , inline , inline2, inline3, inline_eatgame, inline_pans
    inline = InlineKeyboardMarkup()
    inline2 = InlineKeyboardMarkup()
    inline3 = InlineKeyboardMarkup()
    inline_eatgame = InlineKeyboardMarkup()
    inline_pans = InlineKeyboardMarkup()



    b1 = InlineKeyboardButton('Выбрать режим игры', callback_data='button1')
    inline.add(b1)
    b2 = InlineKeyboardButton('Загадки', callback_data='button2')
    inline.add(b2)
    b2new = InlineKeyboardButton('Новая загадка', callback_data='button2new')
    inline2.add(b2new)
    b2end = InlineKeyboardButton('Закончить игру', callback_data='button2end')
    inline2.add(b2end)
    b3 = InlineKeyboardButton('Съедобное 🍽 / Несъедобное 🚫', callback_data='button3')
    inline.add(b3)
    b_p = InlineKeyboardButton('Что на картинке?', callback_data='button_p')
    inline.add(b_p)
    b4 = InlineKeyboardButton('Информация/Помощь', callback_data='button4')
    inline.add(b4)
    b5 = InlineKeyboardButton('Попрощаться с ботом', callback_data='button5')
    inline.add(b5)
    b12 = InlineKeyboardButton('Oтвет', callback_data='button12')
    inline2.add(b12)
    bot.send_message(message.chat.id, 'Вас приветствует Ассистент проекта Робот-тьютор! Выберите что вам надо:', reply_markup=inline)
    b_e = InlineKeyboardButton('Съедобное 🍽', callback_data='button_e')
    inline_eatgame.add(b_e)
    b_une = InlineKeyboardButton('Несъедобное 🚫', callback_data='button_une')
    inline_eatgame.add(b_une)
    b_ende = InlineKeyboardButton('Закончить игру', callback_data='button_ende')
    inline_eatgame.add(b_ende)
    b_pa = InlineKeyboardButton('Ответ', callback_data='button_pa')
    inline_pans.add(b_pa)
    b_pnew = InlineKeyboardButton('Новая картинка', callback_data='button_pnew')
    inline_pans.add(b_pnew)
    b_pend = InlineKeyboardButton('Закончить игру', callback_data='button_pend')
    inline_pans.add(b_pend)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    global otvet , zagad , flag, category, p_answers , ans, photo
    if call.data == 'button1':
        b1a = InlineKeyboardButton('1 режим', callback_data='button1a')
        inline3.add(b1a)
        b1b = InlineKeyboardButton('2 режим', callback_data='button1b')
        inline3.add(b1b)
        bot.send_message(call.message.chat.id, 'Выберите режим игры', reply_markup=inline3)
#############################################################################################################
    elif call.data == 'button2':
        flag = True
        bot.send_message(call.message.chat.id, 'Я скажу Вам загадку, попробуйте отгадать её!')
        bot.send_message(call.message.chat.id, 'Загадка:\n\n'+ str(zagad), reply_markup=inline2)
    elif call.data == 'button12' and flag == True:
        flag = False
        bot.send_message(call.message.chat.id, otvet)
        zagad, otvet = change_zag()
    elif call.data == 'button_2new':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id + 1)
        bot.send_message(call.message.chat.id, 'Загадка:\n\n' + str(zagad))
    elif call.data == 'button_2end':
        bot.send_message(call.message.chat.id, 'Игра приостановлена', reply_markup=inline)
#############################################################################################################
    elif call.data == 'button3':
        category, thing = f_eatgame()
        bot.send_message(call.message.chat.id, '{} - Съедобное 🍽 или Несъедобное 🚫 ?'.format(thing), reply_markup=inline_eatgame)
    elif call.data == 'button_e':
        if category == 'Съедобное 🍽':
            bot.send_message(call.message.chat.id, 'Правильно 😁')
        else:
            bot.send_message(call.message.chat.id, 'Неправильно ☹ Это - несъедобное 🚫 !')
        time.sleep(2)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id + 1)
        category, thing = f_eatgame()
        bot.send_message(call.message.chat.id, '{} - Съедобное 🍽 или Несъедобное 🍽 ?'.format(thing),
                         reply_markup=inline_eatgame)
    elif call.data == 'button_une':
        if category == 'Несъедобное 🚫':
            bot.send_message(call.message.chat.id, 'Правильно 😁')
        else:
            bot.send_message(call.message.chat.id, 'Неправильно ☹ Это съедобное 🚫 !')
        time.sleep(2)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id + 1)
        category, thing = f_eatgame()
        bot.send_message(call.message.chat.id, '{} - Съедобное 🍽 или Несъедобное 🚫 ?'.format(thing),
                         reply_markup=inline_eatgame)
    elif call.data == 'button_ende':
        bot.send_message(call.message.chat.id, 'Игра приостановлена', reply_markup=inline)
#############################################################################################################
    elif call.data == 'button_p':
        bot.send_message(call.message.chat.id, 'Что ты видишь на этой картинке?')
        photo , ans =  f_pictures()
        bot.send_photo(call.message.chat.id, photo, reply_markup=inline_pans)
    elif call.data == 'button_pa':
        bot.send_message(call.message.chat.id, ans)
    elif call.data == 'button_pnew':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id + 1)
        photo , ans =  f_pictures()
        bot.send_photo(call.message.chat.id, photo, reply_markup=inline_pans)
    elif call.data == 'button_pend':
        bot.send_message(call.message.chat.id, 'Игра приостановлена', reply_markup=inline)
#############################################################################################################
    elif call.data == 'button4':
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите. Бот присылает вам видео...')
        video = open('Videobot.mp4', 'rb')
        bot.send_video(call.message.chat.id, video)
        bot.send_message(call.message.chat.id, 'При поддержке pi40.ru\nПоддержка: +7(986)-932-72-06')
#############################################################################################################
    elif call.data == 'button5':
        bot.send_sticker(call.message.chat.id, sticker_gb)
        bot.send_message(call.message.chat.id, 'До скорой встречи, друг! Приятно было с тобой поиграть! :)')
        time.sleep(3)
#############################################################################################################
    elif call.data == 'button1a':
        client.publish(topic, '1')
        bot.send_message(call.message.chat.id, 'Спасибо! Режим выбран')
    elif call.data == 'button1b':
        client.publish(topic, '2')
        bot.send_message(call.message.chat.id, 'Спасибо! Режим выбран')

bot.polling(none_stop=True)




