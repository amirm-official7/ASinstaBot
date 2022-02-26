from instabot import Bot
import schedule
import time
import random
import json

# bot = Bot()
# bot.login(username="amir_m_gamer", password='amir.1221')

with open('massages.json') as f:
    data = json.load(f)


usernames = ['amirm_official7']

goodMorningTime = "10:20"

goodNightTime = "21:15"

questionTime = "12:30"


def goodMorning():
    massage=random.choice(data['goodNightMassages']["massages"])
    bot.send_message(massage, usernames)

def goodNight():
    massage=random.choice(data['goodMorningMassages']["massages"])
    bot.send_message(massage, usernames)

def question():
    massage=random.choice(data['questions']["massages"])
    bot.send_message(massage, usernames)




schedule.every().day.at(goodMorningTime).do(goodMorning)
schedule.every().day.at(questionTime).do(question)
schedule.every().day.at(goodNightTime).do(goodNight)



while True:
    print('run')
    schedule.run_pending()
    time.sleep(59)