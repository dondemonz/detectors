import time
from fixture.work_with_db import DbHelper




def test_light_detector(fixture_for_light):
    db1 = DbHelper(dbname="protocol")
    db1.clean_db()
    time.sleep(9)

    db1.find_light_on()
    db1.find_light_off()




