from aiogram import executor, Dispatcher, types
from Config import dp, scheduler, bot, PATH, PAYMENT_KEY
from Keyboards import *
from Workers import schedule
from DB import DBConn
from asyncio import sleep





@dp.message_handler(commands='start', state='*')
async def channel_list(message: types.Message):
    code = message.get_args()
    if code==PAYMENT_KEY:
        DBConn.StartPremium(message.from_user.id)
        DBConn.CreateUser(message.from_user.id,
                        message.from_user.username,
                        message.from_user.first_name,
                        message.from_user.last_name
                        )
        start_message = '''
Привет, меня зовут Ирина Глушкова👋

Этот бот создан для формирования твоей привычки регулярно вести аккаунт в соц.сетях📱

Спасибо за покупку🔥
Но давай познакомимся поближе⏭️ 
        '''
        await bot.send_message(
        message.from_user.id,
        text=start_message,
        reply_markup=keyboards.start_kb(),
        disable_web_page_preview=False,
        )
    else:
        fail_message ='''
        Привет, меня зовут Ирина Глушкова👋
Этот бот создан для формирования твоей привычки регулярно вести аккаунт в соц.сетях📱
Если вы хотите приобрести мой курс. То можно сделать это здесь👇🏻
        '''
        await bot.send_message(
        message.from_user.id,
        text=fail_message,
        reply_markup=keyboards.goto_buy_kb(),
        disable_web_page_preview=False,
        )
        
        


@dp.callback_query_handler(lambda c: c.data == 'start', state='*')
async def start_callback(call: types.CallbackQuery, ):
    video_text ='''
👇🏻 Держи ссылка на видео, так мы с тобой познакомимся поближе

Скоро тебе придут первые советы,выкладывай их в Stories и отмечай меня у себя❤️
https://youtube.com/shorts/ETiPUgjwWUw?si=r6serbsvL6sFp4pM
    '''
    await bot.send_message(
        call.from_user.id,
        text=video_text,
        reply_markup=keyboards.links_kb(),
        parse_mode=types.ParseMode.HTML,
        disable_web_page_preview=False,
    )
    await sleep(2)

    marathon_text = '''
Марафон "одной привычки"
    
возможность освоить все необходимые навыки для успешного ведения своего блога в социальных сетях📱

<b>За 14 дней ты получишь:</b>

– <b>14 постов</b> у себя в Instagram

– Расширишь охваты своей аудитории и создашь регулярную привычку публиковать контент🌏

– <b>Преодолеешь страх перед ведением социальных сетей</b> в поддерживающем пространстве, а также познакомишься с другими участниками марафона в нашем закрытом телеграмм-канале. 

– Обучалка с помощью коротких видео уроков по CapCut📸

– Будешь выполнять ежедневные задания с предлагаемыми публикациями или рилс🔥

– Будем вместе искать оптимальные алгоритмы инстаграм и наполнять свои аккаунт полезным контентом🔠

Для успешного прохождения марафона ты также получишь <b>личную коучинговую поддержку.</b>

«Дай себе разрешение на новые качественные шаги в развитии своего блога»

Для всех, кому важно начать действовать и внедрять новые шаги📈
    '''
    await bot.send_message(
        call.from_user.id,
        text=marathon_text,
        # reply_markup=keyboards.goto_buy_kb(),
        parse_mode=types.ParseMode.HTML
    )
    
    await sleep(2)
    await bot.send_video_note(
        call.from_user.id,
        video_note=types.InputFile(PATH.parent.joinpath('Circles').joinpath('1.mp4'))
    )
    await sleep(2)
    await bot.send_video_note(
        call.from_user.id,
        video_note=types.InputFile(PATH.parent.joinpath('Circles').joinpath('2.mp4'))
    )

if __name__ == '__main__':
    print('started')
    schedule()
    scheduler.start()
    executor.start_polling(dp, skip_updates=False)
