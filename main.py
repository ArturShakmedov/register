import telebot
from telebot.types import Message, CallbackQuery, LabeledPrice

from database import *
from keybords import *

bot = telebot.TeleBot('7184842777:AAHyEBTUFdKeK0yxfia_-I_p6ljEIvL9hN8')

try:
    create_table_users()
except:
    pass


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    bot.reply_to(message, f'''Я помогу тебе не забыть о твоих планах !\nНо сначала давай пройдём аутентификацию ''')
    register_user(message)


def register_user(message:  Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    user = first_select_user(chat_id)
    if user:
        bot.send_message(chat_id, f'Приветствую вас {full_name}')
    else:
        first_register_user(chat_id, full_name)
        bot.send_message(chat_id, f'Давайте вас авторизуем \n Для регистрации поделитесь Контактом',
                         reply_markup=send_contact_button())


@bot.message_handler(content_types=['contact'])
def finish_register_users(message: Message):
    chat_id = message.chat.id
    phone = message.contact.phone_number
    update_user_finish_register(phone, chat_id)
    bot.reply_to(message, 'Регистрация прошла успешно')


bot.infinity_polling()
