import time
from fixture.work_with_db import DbHelper


def test_tilt_detector(fixture_for_tilt):
    db2 = DbHelper(dbname="protocol")
    db2.clean_db()
    time.sleep(320)
    db2.find_shifted()
