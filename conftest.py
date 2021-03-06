from fixture.load_dll import DllHelper
from model.input_data import *
import pytest
from fixture.take_datetime import *


@pytest.fixture
def fix(request):
    fixture = DllHelper()
    # функция disconnect передается в качестве параметра
    request.addfinalizer(fixture.disconnect)
    return fixture


@pytest.fixture() #scope="session", autouse=True
def fixture_for_defocus(request):
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">,parent_id<" + slave + ">,name<" + grabber_name + ">,type<Virtual>,model<default>,chan<14>").encode("utf-8"))
    #канал у камеры mux, а не grabber_chan и он должен быть на 1 меньше ожидаемого
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + cam_id + ">,parent_id<" + cam_id + ">,name<" + cam_name + ">,,mux<13>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM_DEFOCUS>,objid<" + defocus_id + ">,parent_id<" + defocus_id + ">,name<" + detector_name + ">").encode("utf-8"))
    #object, parent  id: 202, type: CAM_DEFOCUS, id: 1, params: CAM_DEFOCUS | 1 | CREATE | _generated_slave_id < 1 >, cs_computer_name < VQA - 2 >, cs_request_id < 2 >, cs_user_id < root >, cs_user_name < root >, name < 1 >, parent_id < 202 >, slave_id < VQA - 2.9

    #print('\nSome recource')
    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">").encode("utf-8"))
        #print('\nSome resource fin')
    request.addfinalizer(fin)
    return request

@pytest.fixture()
def fixture_for_defocus_shedule(request):
    t2 = take_time1()
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<TIME_ZONE>,objid<1.1>,parent_id<1>,name<Zone>").encode("utf-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<TIME_ZONE>,objid<1.1>,parent_id<1>,name<Zone>,INTERVAL.days.0<127>,INTERVAL.days.count<1>,INTERVAL.time1.0 <00:00:00.000>,INTERVAL.time1.count<1>,INTERVAL.time2.0<" + t2 + ">,INTERVAL.time2.count < 1 >").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">,parent_id<" + slave + ">,name<" + grabber_name + ">,type<Virtual>,model<default>,chan<14>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + cam_id + ">,parent_id<" + cam_id + ">,name<" + cam_name + ">,,mux<13>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM_DEFOCUS>,objid<" + defocus_id + ">,parent_id<" + defocus_id + ">,name<" + detector_name + ">,enable_time_zone<1>,time_zone<1.1>").encode("utf-8"))
    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">").encode("utf-8"))
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<TIME_ZONE>,objid<" + time_zone_id + ">").encode("utf-8"))
    request.addfinalizer(fin)
    return t2

@pytest.fixture()
def fixture_for_light(request):
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">,parent_id<" + slave + ">,name<" + grabber_name + ">,type<Virtual>,model<default>,chan<2>").encode("utf-8"))
    #канал у камеры mux, а не grabber_chan и он должен быть на 1 меньше ожидаемого
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + cam_id + ">,parent_id<" + cam_id + ">,name<" + cam_name + ">,,mux<1>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM_ZONE>,objid<202.2>,parent_id<202>,name<Main_2>").encode("utf-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<CAM_ZONE>,objid<202.2>,mask0<0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFF>,mask1<FFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC000>,mask2<0000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFF>,mask3<FFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC0000000FFFFFFFFFFFFC000>,mask4<000000000000001FC000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000>").encode("utf-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<CAM_ZONE>,objid<202.0>,mask0<FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF>,mask1<FFFFFFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFF>,mask2<FFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE0000000>,mask3<0001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFE00000000001FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF>,mask4<FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<LD>,objid<202.2>,parent_id<202>,name<LD>").encode("utf-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<LD>,objid<202.2>,inner_zone_id<202.0>,outer_zone_id<202.2>,sensitivity<10>").encode("utf-8"))

    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">").encode("utf-8"))
    request.addfinalizer(fin)
    return request


@pytest.fixture()
def fixture_for_tilt(request):
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">,parent_id<" + slave + ">,name<" + grabber_name + ">,type<Virtual>,model<default>,chan<3>").encode("utf-8"))
    #канал у камеры mux, а не grabber_chan и он должен быть на 1 меньше ожидаемого
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + cam_id + ">,parent_id<" + cam_id + ">,name<" + cam_name + ">,,mux<2>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM_DEFOCUS>,objid<" + defocus_id + ">,parent_id<" + defocus_id + ">,name<" + detector_name + ">").encode("utf-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<CAM_DEFOCUS>,objid<202>,shift_detector<1>").encode("utf-8"))


    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">").encode("utf-8"))
    request.addfinalizer(fin)
    return request

@pytest.fixture()
def fixture_for_glare(request):
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">,parent_id<" + slave + ">,name<" + grabber_name + ">,type<Virtual>,model<default>,chan<4>").encode("utf-8"))
    #канал у камеры mux, а не grabber_chan и он должен быть на 1 меньше ожидаемого
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + cam_id + ">,parent_id<" + cam_id + ">,name<" + cam_name + ">,,mux<3>").encode("utf-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<CAM>,objid<202>,blinding<1>").encode("utf-8"))

    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">").encode("utf-8"))
    request.addfinalizer(fin)
    return request

@pytest.fixture()
def fixture_for_glare_shedule(request):
    t2 = take_time2()
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<TIME_ZONE>,objid<1.1>,parent_id<1>,name<Zone>").encode("utf-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<TIME_ZONE>,objid<1.1>,parent_id<1>,name<Zone>,INTERVAL.days.0<127>,INTERVAL.days.count<1>,INTERVAL.time1.0 <00:00:00.000>,INTERVAL.time1.count<1>,INTERVAL.time2.0<" + t2 + ">,INTERVAL.time2.count < 1 >").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">,parent_id<" + slave + ">,name<" + grabber_name + ">,type<Virtual>,model<default>,chan<4>").encode("utf-8"))
    #канал у камеры mux, а не grabber_chan и он должен быть на 1 меньше ожидаемого
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + cam_id + ">,parent_id<" + cam_id + ">,name<" + cam_name + ">,,mux<3>").encode("utf-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<CAM>,objid<202>,blinding<1>,blind_time_zone<1.1>").encode("utf-8"))
    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + cam_id + ">").encode("utf-8"))
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<TIME_ZONE>,objid<" + time_zone_id + ">").encode("utf-8"))
    request.addfinalizer(fin)
    return t2