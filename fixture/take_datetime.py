import datetime as dt
from datetime import timedelta

def take_datetimes():
    m = dt.datetime.now() + timedelta(hours=1)
    starttime = m.strftime("%Y-%m-%d %H:%M:%S")
    m2 = dt.datetime.now() + timedelta(hours=1, seconds=1)
    starttime2 = m2.strftime("%Y-%m-%d %H:%M:%S")
    m3 = dt.datetime.now() + timedelta(hours=1, seconds=2)
    starttime3 = m3.strftime("%Y-%m-%d %H:%M:%S")
    m4 = dt.datetime.now() + timedelta(hours=1, seconds=3)
    starttime4 = m4.strftime("%Y-%m-%d %H:%M:%S")
    return starttime, starttime2, starttime3, starttime4


def take_datetime():
    m = dt.datetime.now()
    t1 = m.strftime("%Y-%m-%d %H:%M:%S")
    return t1

def take_datetime1():
    m = dt.datetime.now() + timedelta(minutes=1)
    t1 = m.strftime("%Y-%m-%d %H:%M:%S")
    return t1

def take_time():
    m = dt.datetime.now()
    t1 = m.strftime("%H:%M:%S")
    return t1

def take_time1():
    m = dt.datetime.now() + timedelta(minutes=1, seconds=30)
    t1 = m.strftime("%H:%M:%S")
    return t1
