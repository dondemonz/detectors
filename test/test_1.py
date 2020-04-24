import time
from fixture.work_with_db import DbHelper
from fixture.take_datetime import *
from fixture.work_with_tree import *


def test_defocus_detector(fix2, fix):
    dlg = expand_tree_to_detector()
    check_dlg_properties(dlg)

    db = DbHelper(dbname="securos")
    db.check_cam_defocus_from_db(db)
    assert db.edge_template == "1"

    db1 = DbHelper(dbname="protocol")
    db1.clean_db()
    dlg.Камерасфокусирована.click()
    dlg.ОК.click()
    #ждем записи в БД
    time.sleep(1)
    db.check_cam_defocus_from_db(db)
    assert db.edge_template < "1"
    t1 = take_datetime()
    #ждем дефокусировки
    time.sleep(25)
    t2 = take_datetime()
    db1.find_defocus_time()
    defocustime = db1.records[0][5]
    defocustime = defocustime.strftime("%Y-%m-%d %H:%M:%S")
    #print(defocustime)
    assert t1 <= defocustime <= t2
    t3 = take_datetime()
    time.sleep(15)
    t4 = take_datetime()

    db2 = DbHelper(dbname="protocol")
    db2.find_focus_time(t2)
    focustime = db2.records[0][5]
    focustime = focustime.strftime("%Y-%m-%d %H:%M:%S")
    #print(focustime)
    assert t3 <= focustime <= t4
    dlg.child_window(auto_id="MainPanelForm.gridLayoutWidget.MainPanelWidget.rightFrame.setupWidget.setupButton").click()

def test_defocus_detector_with_schedule(fix3):
    t1 = take_time()
    db1 = DbHelper(dbname="protocol")
    db1.clean_db()
    dlg = expand_tree_to_detector()
    dlg.Камерасфокусирована.click()
    dlg.ОК.click()
    time.sleep(90)
    db1 = DbHelper(dbname="protocol")
    db1.find_defocus_time()
    defocustime = db1.records[0][5]
    defocustime = defocustime.strftime("%H:%M:%S")
    #print(defocustime)
    #есть ли хотябы 1 дефокус в течение действия таймзоны
    assert t1 <= defocustime <= fix3
    t3 = take_datetime()
    time.sleep(90)
    db2 = DbHelper(dbname="protocol")
    db2.find_defocus_time_after_deactivation_zone(t3)
    # после деактивации таймзоны нет ни одного дефокуса
    assert db2.records == []
    #print(defocustime)
    dlg.child_window(auto_id="MainPanelForm.gridLayoutWidget.MainPanelWidget.rightFrame.setupWidget.setupButton").click()




"""

def focus_cam(fix):
    time.sleep(2)
    fix.send_react(("CAM|202|FOCUS_OUT|__domain<>,__host<VQA-2>,__user<root>,_generated_slave_id<1>,original_slave_id<VQA-2.MediaClient.1`3>,priority<2147483647>,slave_id<VQA-2.MediaClient.1`5>,user_host<VQA-2>,user_id<root>").encode("utf-8"))
    time.sleep(2)
    fix.send_react(("CAM|202|FOCUS_STOP|__domain<>,__host<VQA-2>,__user<root>,_generated_slave_id<1>,original_slave_id<VQA-2.MediaClient.1`3>,priority<2147483647>,slave_id<VQA-2.MediaClient.1`5>,speed<5>,user_host<VQA-2>,user_id<root>").encode("utf-8"))
    time.sleep(1)
"""
    #p.print_control_identifiers()
    #check_time < 2 >, delta_sharpness < 15 >, edge_template < 0.09782166280864198 >, enable_time_zone < 0 >, flags <>, grabber_id < 9 >, name <  1 >, original_slave_id <>, parent_id < 9 >, shift_detector < 0 >, time_zone <>, zone_rect_h < 100 >, zone_rect_w < 100 >, zone_rect_x < 0 >, zone_rect_y < 0 >

    #n = p.element_value
    #elements = pywinauto.findwindows.find_element(auto_id="MainPanelForm.ObjectEditorWidget.DefocusDetector.sbSensitivity")

    #print(dlg.Компьютер.dump_tree())

# fix.send_react(("CAM_DEFOCUS|202|SETUP|check_time<3>,delta_sharpness<15>,edge_template<0.09782166280864198>,enable_time_zone<0>,flags<>,grabber_id<202>,name<cam 202>,original_slave_id<>,parent_id<202>,shift_detector<0>,time_zone<>,zone_rect_h<100>,zone_rect_w<100>,zone_rect_x<0>,zone_rect_y<0>").encode("utf-8"))
# fix.send_react(("CAM_DEFOCUS|202|SETUP|check_time<3>,parent_id<202>").encode("utf-8"))
# fix.send_react(("CAM_DEFOCUS|"+camId+"|SETUP").encode("utf-8"))
# fix.send_react(("CAM|202|FOCUS_AUTO_MODE|__domain<>,__host<VQA-2>,__user<root>,_generated_slave_id<1>,original_slave_id<VQA-2.MediaClient.1`5>,priority<2147483647>,slave_id<VQA-2.MediaClient.1`5>,speed<5>,user_host<VQA-2>,user_id<root>").encode("utf-8"))
# fix.send_event(message=(("CORE||UPDATE_OBJECT|objtype<CAM_DEFOCUS>,objid<" + camId + ">,parent_id<202>,check_time<3>").encode("utf-8")))
# fix.send_react(("MEDIA_CLIENT|1|ADD_SEQUENCE|mode<1x1>,seq<|" + camId + ">").encode("UTF-8"))
# fix.send_react(("MEDIA_CLIENT|1|ACTIVATE_CAM|cam<" + camId + ">").encode("UTF-8")
#fix.send_react(("CAM|202|FOCUS_AUTO_MODE|__domain<>,__host<VQA-2>,__user<root>,_generated_slave_id<1>,original_slave_id<VQA-2.MediaClient.1`3>,priority<2147483647>,slave_id<VQA-2.MediaClient.1`3>,user_host<VQA-2>,user_id<root>").encode("utf-8"))
