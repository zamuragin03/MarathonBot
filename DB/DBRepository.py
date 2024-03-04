from datetime import datetime
import csv
import os
import sqlite3
from pathlib import Path
DIR = Path(__file__).parent




class DBRepository:
    def __init__(self):
        self.db = sqlite3.connect(DIR.joinpath('data.db'))
        # self.cur = self.db.cursor()

    def INIT_DB(self):
        videos = os.listdir(DIR.parent.joinpath('Videos'))
        print(videos)

    def CreateUser(self, external_id, username, first_name, last_name):
        cur = self.db.cursor()
        cur.execute(
            f'select*from users where external_id = "{external_id}" ')
        data = cur.fetchone()
        if data is None:
            cur.execute(
                f'insert into users(id,external_id,username,first_name,second_name) values (null, {external_id}, "{username}","{first_name}", "{last_name}") ')
            self.db.commit()

    def StartPremium(self, external_id):
        cur = self.db.cursor()
        res = cur.execute(
            f'select*from users where external_id = "{external_id}" ')
        user = res.fetchone()
        premium_cur = self.db.cursor()
        has_premium_query =f'''
        SELECT * FROM premium
INNER JOIN users ON premium.user_id = users.id
where users.external_id={external_id}
        '''
        
        if len(premium_cur.execute(has_premium_query).fetchall())==1:
            return
        sub_start = datetime.now().timestamp()
        premium = premium_cur.execute(
            f'insert into premium(id, user_id, sub_start) values (null,{user[0]}, {sub_start})')
        self.db.commit()

    def generate_numbers(n):
        return (n*3, n*3 + 3)

    def TextsTaskAt10AM(self,):
        texts_length = len(DBRepository.GetAllTexts())
        query = f'''
SELECT * FROM premium
INNER JOIN users ON premium.user_id = users.id
where premium.sent_texts_count<14
        '''
        cur = self.db.cursor()
        data = cur.execute(query)
        data = data.fetchall()
        return_list = []
        for user in data:
            return_list.append(
                {
                    'external_id': user[6],
                    'indexes': DBRepository.generate_numbers(user[2])
                }
            )
        return return_list
    
    def VideoTaskAt2PM(self,):
        
        query = f'''
SELECT * FROM premium
INNER JOIN users ON premium.user_id = users.id
where premium.sent_videos_count<12
        '''
        cur = self.db.cursor()
        data = cur.execute(query)
        data = data.fetchall()
        return_list = []
        for user in data:
            return_list.append(
                {
                    'external_id': user[6],
                    'index': user[3]
                }
            )
        return return_list

    def IncrementSentTexts(self, extenal_id):
        query = f'''
SELECT * FROM premium
INNER JOIN users ON premium.user_id = users.id
where users.external_id={extenal_id}
        '''
        cur = self.db.cursor()
        data = cur.execute(query)
        data = data.fetchone()
        sent_count = data[2]
        sent_count += 1
        user_id = data[1]
        update_query = f'''
UPDATE premium
SET sent_texts_count = {sent_count}
WHERE user_id = {user_id}
        '''
        cur.execute(update_query)
        self.db.commit()
        
    def IncrementSentVideo(self, extenal_id):
        query = f'''
SELECT * FROM premium
INNER JOIN users ON premium.user_id = users.id
where users.external_id={extenal_id}
        '''
        cur = self.db.cursor()
        data = cur.execute(query)
        data = data.fetchone()
        sent_count = data[3]
        sent_count += 1
        user_id = data[1]
        update_query = f'''
UPDATE premium
SET sent_videos_count = {sent_count}
WHERE user_id = {user_id}
        '''
        cur.execute(update_query)
        self.db.commit()

    def GetTextsByIndex(start, end):
        return DBRepository.GetAllTexts()[start: end]

    def GetAllTexts():
        with open(DIR.joinpath('texts.txt'), 'r') as file:
            data = file.read().split(';')
            data = [item.strip() for item in data if item != '']
            return data
    
    '''
3 день – 1 видео
7 день – 2 видео
11 день – 3 видео
'''
    def GetVideoIndex(day):
        res = {
            3:0,
            7:1,
            11:2
        }
        try:
            return res[day]
        except:
            return -1
        
    def CheckSubscriptionIsOver(self, external_id):
        over_cur = self.db.cursor()
        over_query = f'''
SELECT * FROM premium
INNER JOIN users ON premium.user_id = users.id
where premium.sent_texts_count=13 and users.external_id={external_id}
        '''
        return len(over_cur.execute(over_query).fetchone())!=0

DBConn = DBRepository()
