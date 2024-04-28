from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def send_contact_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = KeyboardButton(text='Поделится контактом', request_contact=True)
    markup.row(buttons_1)
    return markup
