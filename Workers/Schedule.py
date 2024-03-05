from datetime import datetime
from aiogram import Dispatcher, types
from DB import DBConn, DBRepository
from Config import scheduler, dp, bot, PATH, VIDEO_TEXTS

def schedule():
    scheduler.add_job(video_func, 'cron', hour=14, args=(dp,), misfire_grace_time=1000)
    scheduler.add_job(text_func, 'cron', hour=10, args=(dp,), misfire_grace_time=1000)


final_message= '''
Добрый день, к сожалению,наш марафон <tg-spoiler>закончился😢</tg-spoiler>

Нам было приятно видеть вашу заинтересоваться в этом проекте❤️
А это самое главное 🔥

Но также нам с Ириной очень важно знать ваше мнение по поводу марафона:
-что понравилось или же не понравилось? 
-чего не хватало?
-что стоит добавить?
-Ваше ощущение на протяжение всего марафона (побороли ли во страх проявляться в соц.сетях,как вырос ваш аккаунт и тд)

Любая критика будь она положительная или отрицательная, дает толчок только вперед📈

Большое спасибо за участие,увидимся в следующих проектах📽️❤️
'''

async def text_func(dp: Dispatcher):
    premium_users = DBConn.TextsTaskAt10AM()
    for user in premium_users:
        indexes = user.get('indexes')
        texts = DBRepository.GetTextsByIndex(indexes[0], indexes[1])
        for text in texts:
            try:
                await bot.send_message(
                user.get('external_id'),
                text
            )
            except :
                ...
        if DBConn.CheckSubscriptionIsOver(user.get('external_id')):
            try:
                await bot.send_message(
            user.get('external_id'),
            final_message,
            parse_mode='html'
            )
            except:
                ...
        DBConn.IncrementSentTexts(user.get('external_id'))
        
        
async def video_func(dp: Dispatcher):
    premium_users = DBConn.VideoTaskAt2PM()
    for user in premium_users:
        index = user.get('index')
        video_index= DBRepository.GetVideoIndex(index)
        if (video_index!=-1):
            try:
                await bot.send_video(
                user.get('external_id'),
                video=types.InputFile(PATH.parent.joinpath('Videos').joinpath(f'{video_index+1}.mov')),
                caption=VIDEO_TEXTS[video_index]
            )
            except:
                ...
        DBConn.IncrementSentVideo(user.get('external_id'))
    
