import configparser
from pathlib import Path
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging

config = configparser.ConfigParser()

PATH = Path(__file__).resolve().parent
config.read(str(PATH) + '/config.ini')
BOT_TOKEN = config['Telegram']['bot_token']
PAYMENT_KEY = config['Telegram']['payment_key']
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
scheduler = AsyncIOScheduler()
logger = logging.getLogger(__name__)
logging.basicConfig(filename="debug.log", filemode="w", level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s', )
import pytz
desired_timezone = 'Europe/Moscow'
timezone_obj = pytz.timezone(desired_timezone)

import os
import time

# Set your desired timezone (e.g., Europe/Moscow for UTC+3)
os.environ['TZ'] = 'Europe/Moscow'
time.tzset()

VIDEO_TEXTS =[
    '''
1 ВИДЕОУРОК

Первый видеоурок посвящен базовым вещам в CapCut

Сегодня вы узнаете:
💙Как добавлять видеоматериал в приложение 
💙Как легко и просто разделить и удалить объект 
💙Сделать классный переход 
💙Как одним касанием убрать весь звук на всех видео
💙Как убрать выплывающий значок CapCut в конце и тд

Если будет что-то не понять можете писать в общей беседе вопрос✔ 
    ''',
    '''
2 ВИДЕОУРОК

Второй видеоурок посвящен музыке в CapCut

Сегодня вы узнаете:
💙Как добавлять музыку 
💙Как легко и просто сделать биты 
💙Как добавить музыку из браузера
💙Как сделать плавное угасание музыки

Если будет что-то не понять можете писать в общей беседе вопрос  или в комментариях✔ 

Либо же лично мне в личные сообщения (@katush0)💟
    ''',
    '''
3 ВИДЕОУРОК

Третий видеоурок посвящен текста и автоматических субтитрах в CapCut

Сегодня вы узнаете:
💙Как добавлять текст
💙Как изменить стиль текста
💙Как добавить плавный переход текста
💙Как добавить стикеры
💙Ну и самое главное добавление автоматических субтитров на вашу озвучка

Если будет что-то не понять можете писать в общей беседе вопрос  или в комментариях✔ 

Либо же лично мне в личные сообщения (@katush0)💟
    '''
]