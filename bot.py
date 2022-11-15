import telebot;
from telebot import types
bot = telebot.TeleBot('');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "/start":
    bot.send_message(message.from_user.id, "Калькулятор рациональных чисел. Чтобы посмотреть, что я умею  /help")
  elif message.text == "/help":
    bot.send_message(message.from_user.id, "Умножение  /multiple")
    bot.send_message(message.from_user.id, "Деление  /division")
    bot.send_message(message.from_user.id, "Сложение  /addition")
    bot.send_message(message.from_user.id, "Вычитание  /subtraction")
  elif message.text == '/multiple':
    bot.send_message(message.from_user.id, "Введите два числа через пробел (для двоичных чисел используйте .)");
    bot.register_next_step_handler(message, get_multiple);
  elif message.text == '/division':
    bot.send_message(message.from_user.id, "Введите два числа через пробел (для двоичных чисел используйте .)");
    bot.register_next_step_handler(message, get_division);
  elif message.text == '/addition':
    bot.send_message(message.from_user.id, "Введите два числа через пробел (для двоичных чисел используйте .)");
    bot.register_next_step_handler(message, get_addition);
  elif message.text == '/subtraction':
    bot.send_message(message.from_user.id, "Введите два числа через пробел (для двоичных чисел используйте .)");
    bot.register_next_step_handler(message, get_subtraction);
  else:
    bot.send_message(message.from_user.id, "Ошибка /help")

def get_multiple(message):
  a = 0;
  b = 0;
  answer = "";
  mestext = message.text;
  if (mestext.find(' ') != -1):
    text = mestext.split(' ');
    try:
        a = float(text[0]);
        b = float(text[1]);
        answer = 'Результат '+str(a*b);
        bot.send_message(message.from_user.id, text=answer)
    except:
        bot.send_message(message.from_user.id, "Ошибка: Введите числа")
  else:
    bot.send_message(message.from_user.id, "Ошибка: Введите два числа через пробел")

def get_division(message):
  a = 0;
  b = 0;
  answer = "";
  mestext = message.text;
  if (mestext.find(' ') != -1):
    text = mestext.split(' ');
    try:
        a = float(text[0]);
        b = float(text[1]);
        answer = 'Результат '+str(a/b);
        bot.send_message(message.from_user.id, text=answer)
    except:
        bot.send_message(message.from_user.id, "Ошибка: Введите числа")
  else:
    bot.send_message(message.from_user.id, "Ошибка: Введите два числа через пробел")

def get_addition(message):
  a = 0;
  b = 0;
  answer = "";
  mestext = message.text;
  if (mestext.find(' ') != -1):
    try:
        a = float(text[0]);
        b = float(text[1]);
        answer = 'Результат '+str(a+b);
        bot.send_message(message.from_user.id, text=answer)
    except:
        bot.send_message(message.from_user.id, "Ошибка: Введите числа")
  else:
    bot.send_message(message.from_user.id, "Ошибка: Введите два числа через пробел")

def get_subtraction(message):
  a = 0;
  b = 0;
  answer = "";
  mestext = message.text;
  if (mestext.find(' ') != -1):
    try:
        a = float(text[0]);
        b = float(text[1]);
        answer = 'Результат '+str(a-b);
        bot.send_message(message.from_user.id, text=answer)
    except:
        bot.send_message(message.from_user.id, "Ошибка: Введите числа")
  else:
    bot.send_message(message.from_user.id, "Ошибка: Введите два числа через пробел")

bot.polling(none_stop=True, interval=0)

