from instabot import Bot
import schedule
import time
import random
import json

with open('info.json') as f:
    data = json.load(f)


bot = Bot()
bot.login(username=data['login']["username"], password=data['login']["password"])




def goodMorning():
    massage=random.choice(data['goodNightMassages']["massages"])
    bot.send_message(massage, data['usernames'])

def goodNight():
    massage=random.choice(data['goodMorningMassages']["massages"])
    bot.send_message(massage, data['usernames'])

def question():
    massage=random.choice(data['questions']["massages"])
    bot.send_message(massage, data['usernames'])




schedule.every().day.at(data['goodMorningMassages']["time"]).do(goodMorning)
schedule.every().day.at(data['questions']["time"]).do(question)
schedule.every().day.at(data['goodNightMassages']["time"]).do(goodNight)



while True:
    print('run')
    schedule.run_pending()
    time.sleep(59)