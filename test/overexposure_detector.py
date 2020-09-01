import time
from fixture.load_dll import DllHelper
from model.input_data import *
import pytest
departmentId = "1.999"
objId = "999"
personId = "9"
camId2 = "10"


@pytest.fixture
def fix(request):
    fixture = DllHelper()
    # функция disconnect передается в качестве параметра
    request.addfinalizer(fixture.disconnect)
    return fixture


def test(request):
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<DEPARTMENT>,objid<"+departmentId+">,parent_id<1>,name<Test_Department>").encode("utf-8"))
    time.sleep(1)
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<PERSON>,objid<1.999>,parent_id<"+departmentId+">,name<"+user2+">,passwd2<"+password2+">").encode("utf-8"))
    time.sleep(1)
    """
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<RTSP_SERVER>,objid<"+objId+">,parent_id<"+slave+">,name<Test_RTSP_Server>,").encode("utf-8"))  # "CAM.cam.count", 1, "CAM.cam.0", GetCamera()
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<RTSP_SERVER>,objid<" + objId + ">,parent_id<" + slave + ">,CAM.cam.count<1>,CAM.cam.0<" + camId + ">").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<ARCH_CNV>,objid<"+objId+">,parent_id<"+slave+">,name<Test_Archive_Converter>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<EVENT_FILTER>,objid<"+objId+">,parent_id<1>,name<Test_Event_Filter>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<IMAGE_EXPORT>,objid<"+objId+">,parent_id<"+slave+">,name<Test_Image_Processor>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<HTTP_EVENT_PROXY>,objid<"+objId+">,parent_id<"+slave+">,name<Test_HTTP_Event_Gate>,port<88>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<REST_API>,objid<"+objId+">,parent_id<"+slave+">,name<Test_RestAPI>").encode("utf-8"))
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<REST_API>,objid<" + objId + ">,parent_id<" + slave + ">,event_filter_id<"+objId+">,port<"+restPort+">").encode("utf-8"))
    fix.send_event(message=(("CORE||UPDATE_OBJECT|objtype<EVENT_FILTER>,objid<" + objId + ">,parent_id<1>,EVENT.action.count<1>,EVENT.type.count<1>,EVENT.id.count<1>,EVENT.rule.count<1>,EVENT.rule.0<1>,EVENT.id.0<>,EVENT.type.0<>,EVENT.action.0<>").encode("utf-8")))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<"+objId+">,parent_id<"+slave+">,name<Grabber_for_delete>,type<Axis>").encode("utf-8"))  # type=Axis, т.к. без типа будет сильно грузиться система
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<"+objId+">,parent_id<"+objId+">,name<Cam_for_delete>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + camId + ">,parent_id<" + slave + ">,name<"+camName+">,type<ONVIF>,model<default>,format<H264>,ip<172.16.16.25>,user_name<service>,auth_crpt<ONAOECDBDDPNLNJBLOMAMOCDLEMNDOHN>").encode("utf-8"))  # type=Axis, т.к. без типа будет сильно грузиться система
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + camId + ">,parent_id<" + camId + ">,name<"+camName+">,telemetry_id<native>").encode("utf-8"))
    """

    fix.send_event(message="CORE||DELETE_OBJECT|objtype<PERSON>,objid<1.999>".encode("utf-8"))
    #time.sleep(1)
    fix.send_event(message="CORE||DELETE_OBJECT|objtype<DEPARTMENT>,objid<1.999>".encode("utf-8"))
    """
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<RTSP_SERVER>,objid<" + objId + ">").encode("utf-8"))
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<ARCH_CNV>,objid<" + objId + ">").encode("utf-8"))
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<EVENT_FILTER>,objid<" + objId + ">").encode("utf-8"))
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<IMAGE_EXPORT>,objid<" + objId + ">").encode("utf-8"))
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<HTTP_EVENT_PROXY>,objid<" + objId + ">").encode("utf-8"))
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<REST_API>,objid<" + objId + ">").encode("utf-8"))
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + camId + ">").encode("utf-8"))
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + camId2 + ">").encode("utf-8"))
    """
    fix.disconnect()
    return request

