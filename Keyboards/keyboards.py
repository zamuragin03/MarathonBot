
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def start_kb():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'Начать', callback_data='start'),

            ]
        ]
    )
    return markup


def links_kb():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f'Бизнес Коуч Телеграмм', url='https://t.me/glushkovacoach',  callback_data='tg_cb'),
            ],
            [
                InlineKeyboardButton(
                    text=f'Бизнес Коуч Инстаграм', url='https://www.instagram.com/irinacoach7?igsh=MXZ5ZWE5NnY5NmhtZA%3D%3D&utm_source=qr',  callback_data='ig_cb'),
            ],

        ]
    )
    return markup


def goto_buy_kb():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f'Записаться на марафон', url='https://t.me/glushkovacoach' ),
            ],
        ]
    )
    return markup

def create_payment_kb():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f'Купить',  callback_data='create_payment'),
            ],
        ]
    )
    return markup

def payment_link_kb(url):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f'Перейти к оплате', url=url, callback_data='check_payment'),
            ],
        ]
    )
    return markup
