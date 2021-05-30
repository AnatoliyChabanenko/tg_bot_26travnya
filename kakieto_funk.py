import json
from datetime import datetime
from my_text import Text
text = Text()

from aiogram import types

from bot2 import db, bot


async def send_all():
    subscriptions = db.get_subscriptions()
    prise = read_json()
    print(subscriptions)
    data = datetime.today().strftime("%d.%m.%Y")

    for user in subscriptions:
        print(user)
        try: await bot.send_message(user[1], text.prise_rozsilka(data,prise), disable_notification=True)
        except:
            print('пользователь заблокировал ')


def admin_validate(message: types.Message)-> bool:
    admin_many = db.get_admin()
    for admin in admin_many:
        if admin[1] == str(message.from_user.id):
            return True

def user_subskribe(message: types.Message) ->bool:
    user = db.get_user(message.from_user.id)
    print(user)
    if db.get_user(message.from_user.id):
        user = db.get_user(message.from_user.id)
        if user[0][2] == 1:
            return True

def read_json():
    utput_json = json.load(open('data1.json'))
    return ("\n".join("🌿{}\t{}грн/т".format(k, v) for k, v in utput_json.items()))

def vremya():
    data = datetime.now().hour
    if 8 < int(data) < 17 :
        return True

if __name__ == '__main__':
    pass
