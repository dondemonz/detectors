import time
from fixture.work_with_db import DbHelper
from fixture.take_datetime import *

def test_glare_detector(fixture_for_glare):
    db4 = DbHelper(dbname="protocol")
    db4.clean_db()
    time.sleep(30)
    db4.find_blinding()
    db4.find_unblinding()
    time.sleep(1)

def test_glare_detector_with_schedule(fixture_for_glare_shedule):
    t1 = take_time()
    db5 = DbHelper(dbname="protocol")
    db5.clean_db()
    time.sleep(30)
    db5 = DbHelper(dbname="protocol")
    db5.find_blinding_time()

    blindingtime = db5.records[0][5]
    blindingtime = blindingtime.strftime("%H:%M:%S")
    #print(blindingtime)
    #есть ли хотябы 1 blinding в течение действия таймзоны
    assert t1 <= blindingtime <= fixture_for_glare_shedule

    t3 = take_datetime()
    time.sleep(40)
    db5 = DbHelper(dbname="protocol")
    db5.find_blinding_time_after_deactivation_zone(t3)
    # после деактивации таймзоны нет ни одного blinding
    assert db5.records == []
