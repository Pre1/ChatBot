import requests
import threading
from random import random
from math import floor
import re
import time
from datetime import datetime


baseURL = 'https://api-chatr.herokuapp.com'
COF_CH_ID = 159

KEYWORDS = [
    "coffeeee",
    "☕️",
]

RESPONSES = [
    "did I hear coffee ?! here ☕️",
    "here ☕️ :)",
    "sorry currently I'm serving my master...",
    "nope, no coffee for you...",
    "one sec... the water is bolling",
    "oh shit! I don't run out of coffee beans!",
]


def random_res(ls, username):
    return "@{} {}".format(username, ls[floor(random() * len(ls))])


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def login():
    payload = {
        "username": "coffeeBot",
        "password": "133"
    }

    r = requests.post(baseURL + '/login/', data=payload)

    return r.json()['token']


token = login()


def postMsg(str, chId=COF_CH_ID):
    requests.post(
        baseURL + '/channels/%d/send/' % (chId),
        headers={'authorization': 'JWT ' + token},
        data={"message": str}
    )


def getAllChannels(id):
    data = requests.get(
        baseURL + '/channels/%d/' % (id),
        headers={'authorization': 'JWT ' + token}
    )
    return data.json()


def run():
    while True:
        lastMsg = getAllChannels(COF_CH_ID)[-1]
        msg = lastMsg['message']
        match = re.search("cof+e+", msg)

        allowCmds = ['/cal', '/post', '/today', "/help"]
        cmdMatch = msg.split(' ')

        print(lastMsg)

        if ((cmdMatch[0][0] == "/") and (cmdMatch[0] in allowCmds) and (lastMsg['username'] == 'pre1' or lastMsg['username'] == 'ayman')):
            cmd = cmdMatch[0]

            if cmd == '/post':
                num_msgs = int(cmdMatch[1])

                slep = int(cmdMatch[2])

                # id=<chID>
                chId = int(cmdMatch[3].split('=')[1]) if (
                    "id" in cmdMatch[3]) else (COF_CH_ID)

                # msg=<your message>
                msg = (" ".join(cmdMatch[4:])) if (
                    len(cmdMatch) > 4) else "test ️️☕️"

                if chId != COF_CH_ID:
                    postMsg("Ok, I'll go there")

                for _ in range(num_msgs):
                    postMsg(msg, chId)
                    time.sleep(slep)

            elif cmd == '/cal':
                msg = cmdMatch[1]
                postMsg(eval(msg))

            elif cmd == '/today':
                now = datetime.now()
                msg = now.strftime("%m/%d/%Y, %H:%M:%S")
                postMsg("today's date: " + msg)

            elif cmd == '/help':
                helpstr = """Commmnds:
                '/cal': eg: `/cal 1+23+1` no spaces between math operations.
                '/today': to show today's date (hey Mr Obvious)
                '/post': post (number of messages) (wait time betwreen each msg in sec)
                        (Channel ID: `id=<ch_id>` or `-` to post the default channel)
                        (your messgge)

                        eg: /post 2 3 - test
                            => this will post 2 msgs, wait 3 sec between
                            each msg, it'll be posted in the current channel 
                            and the message will be `test`. 

                        eg: /post 2 3 id=123 test
                            => same thing as the above but it'll be posted
                            to a channel with ID of `123`
                """
                print(helpstr)
                postMsg(helpstr)
            else:
                postMsg("sorry I don't know that one, how about a cup of coffee?")

        elif ((match or "☕️" in msg) and (lastMsg['username'] != "coffeeBot")):
            postMsg(random_res(RESPONSES, lastMsg['username']))
            time.sleep(1)

        else:
            print("msg: ", msg)

        time.sleep(1)

# set_interval(run, 4)


run()
