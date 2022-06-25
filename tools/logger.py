import datetime


def log(msg):
    cur_time = datetime.datetime.now()
    s = "[" + str(cur_time) + "]" + msg
    print(s)
