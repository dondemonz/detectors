from fixture.load_dll import DllHelper
from model.input_data import *
import pytest
import time
from fixture.take_datetime import *


@pytest.fixture
def fix(request):
    fixture = DllHelper()
    # функция disconnect передается в качестве параметра
    request.addfinalizer(fixture.disconnect)
    return fixture


@pytest.fixture() #scope="session", autouse=True
def fix2(request):
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + camId + ">,parent_id<" + slave + ">,name<" + grabberName + ">,type<Virtual>,model<default>,chan<14>").encode("utf-8"))
    time.sleep(1)
    #канал у камеры mux, а не grabber_chan и он должен быть на 1 меньше ожидаемого
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + camId + ">,parent_id<" + camId + ">,name<"+camName+">,,mux<13>").encode("utf-8"))
    time.sleep(1)
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM_DEFOCUS>,objid<" + defocusId + ">,parent_id<" + defocusId + ">,name<" + detectorName + ">").encode("utf-8"))
    #object, parent  id: 202, type: CAM_DEFOCUS, id: 1, params: CAM_DEFOCUS | 1 | CREATE | _generated_slave_id < 1 >, cs_computer_name < VQA - 2 >, cs_request_id < 2 >, cs_user_id < root >, cs_user_name < root >, name < 1 >, parent_id < 202 >, slave_id < VQA - 2.9

    #print('\nSome recource')
    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + camId + ">").encode("utf-8"))
        #print('\nSome resource fin')
        fix.disconnect()
    request.addfinalizer(fin)
    return request

@pytest.fixture()
def fix3(request):
    t2 = take_time1()
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<TIME_ZONE>,objid<1.1>,parent_id<1>,name<Zone>").encode("utf-8"))
    time.sleep(1)
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<TIME_ZONE>,objid<1.1>,parent_id<1>,name<Zone>,INTERVAL.days.0<127>,INTERVAL.days.count<1>,INTERVAL.time1.0 <00:00:00.000>,INTERVAL.time1.count<1>,INTERVAL.time2.0<" + t2 + ">,INTERVAL.time2.count < 1 >").encode("utf-8"))
    time.sleep(1)
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + camId + ">,parent_id<" + slave + ">,name<" + grabberName + ">,type<Virtual>,model<default>,chan<14>").encode("utf-8"))
    time.sleep(1)
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + camId + ">,parent_id<" + camId + ">,name<" + camName + ">,,mux<13>").encode("utf-8"))
    time.sleep(2)
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM_DEFOCUS>,objid<" + defocusId + ">,parent_id<" + defocusId + ">,name<" + detectorName + ">,enable_time_zone<1>,time_zone<1.1>").encode("utf-8"))
    def fin():
        #fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + camId + ">").encode("utf-8"))
        time.sleep(1)
        #fix.send_event(message=("CORE||DELETE_OBJECT|objtype<TIME_ZONE>,objid<"+timeZoneId+">").encode("utf-8"))
        fix.disconnect()
    request.addfinalizer(fin)
    return t2
