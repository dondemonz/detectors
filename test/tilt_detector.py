import time
from fixture.work_with_db import DbHelper


def test(fix5):
    db2 = DbHelper(dbname="protocol")
    db2.clean_db()
    time.sleep(320)
    db2.find_shifted()
