import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/start")
    item2 = types.KeyboardButton("/status")
    item3 = types.KeyboardButton("/help")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы конвертировать файлы формата FPX/FRX в любой доступный. Просто добавить сюда необходимый файл".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):

    sti = open('static/negr.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/start")
    item2 = types.KeyboardButton("/status")
    item3 = types.KeyboardButton("/help")

    markup.add(item1, item2, item3)


    bot.send_message(message.chat.id,
                     "Мы бы тоже хотели попросить помощи\n\nбот-конвертер 'Суетологи'\n\nИнформация про команду:\nДарья - \nРуслан - \nСтас - \nКостя - \nДанила - \n\nСсылка на FastReports - https://fastreport.cloud\n\nСписок доступных команд\n/start\n/help\n/status\n".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['status'])
def status(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/start")
    item2 = types.KeyboardButton("/status")
    item3 = types.KeyboardButton("/help")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Извините, данная функиця будет в будущем)".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
#def lalala(message):
 #   if message.chat.type == 'private':
  #      if message.text == '/start':
   #         bot.send_message(commands=['start'])
    #    elif message.text == '/status':
     #       bot.send_message(commands=['status'])
      #  elif message.text == '/help':
       #     bot.send_message(commands=['help'])



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)