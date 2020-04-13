import pytest
from model.input_data import *
from pywinauto.application import Application
import time
import pywinauto

def test_1(fix2, fix):
    #fix.send_react(("CAM_DEFOCUS|202|SETUP|check_time<3>,delta_sharpness<15>,edge_template<0.09782166280864198>,enable_time_zone<0>,flags<>,grabber_id<202>,name<cam 202>,original_slave_id<>,parent_id<202>,shift_detector<0>,time_zone<>,zone_rect_h<100>,zone_rect_w<100>,zone_rect_x<0>,zone_rect_y<0>").encode("utf-8"))
    #fix.send_react(("CAM_DEFOCUS|202|SETUP|check_time<3>,parent_id<202>").encode("utf-8"))
    #fix.send_react("CORE", "RANDOM", "CREATE_OBJECT", "objtype", "CAM", "objid", "999999", "parent_id", "2", "name", "Test Camera")
    #fix.send_react(("CAM_DEFOCUS|"+camId+"|SETUP").encode("utf-8"))
    #fix.send_react(("CAM|"+camId+"|ARM").encode("utf-8"))
    app = Application(backend="uia").connect(title='Панель управления SecurOS Enterprise')
    dlg = app.window(title='Панель управления SecurOS Enterprise')
    dlg.child_window(auto_id="MainPanelForm.gridLayoutWidget.MainPanelWidget.rightFrame.setupWidget.setupButton").click()
    #dlg.child_window(title="Компьютер VQA-2 [VQA-2]", control_type="TreeItem").print_control_identifiers()

    expand_tree_to_detector(dlg)
    dlg.Камерасфокусирована.click()
    time.sleep(3)
    dlg.ОК.click()
    time.sleep(3)
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<CAM_DEFOCUS>,objid<" + camId + ">").encode("utf-8"))
    time.sleep(3)
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM_DEFOCUS>,objid<" + camId + ">,parent_id<" + camId + ">,name<" + detectorName + ">").encode("utf-8"))
    #dlg.child_window(title="det 202 [202]", control_type="TreeItem").double_click_input()

    #MainPanelForm.ObjectEditorWidget.DefocusDetector.sbSensitivity

    #dlg.child_window(auto_id="MainPanelForm.ObjectEditorWidget").OK.click()
    #app.OK.click_input()
    #dlg.Устройства.double_click_input()
    #dlg.cam202.double_click_input()
    #dlg.camr202.double_click_input()
    #ef = dlg.Оповещение.MMS.Exists(timeout=1)
    #d = dlg.child_window(auto_id="MainPanelForm.gridLayoutWidget.MainPanelWidget.rightFrame.setupWidget.setupButton").click()

    #dlg.ИнтеграцияиАвтоматизация.click_input()
    #time.sleep(1)
    #app.window_().print_control_identifiers()

    #check_time < 2 >, delta_sharpness < 15 >, edge_template < 0.09782166280864198 >, enable_time_zone < 0 >, flags <>, grabber_id < 9 >, name <  1 >, original_slave_id <>, parent_id < 9 >, shift_detector < 0 >, time_zone <>, zone_rect_h < 100 >, zone_rect_w < 100 >, zone_rect_x < 0 >, zone_rect_y < 0 >

    print("1")

def test2222(fix):
    fix.send_event(message=(("CORE||UPDATE_OBJECT|objtype<CAM_DEFOCUS>,objid<" + camId + ">,parent_id<202>,check_time<3>").encode("utf-8")))






def test1222():
    app = Application(backend="uia").connect(title='Панель управления SecurOS Enterprise')
    dlg = app.window(title='Панель управления SecurOS Enterprise')
    p = dlg.child_window(auto_id="MainPanelForm.ObjectEditorWidget.DefocusDetector.sbSensitivity")
    #l = dlg.child_window(auto_id="MainPanelForm.ObjectEditorWidget")
    #p.print_control_identifiers()
    n = p.legacy_properties()['Value']
    print(n)
    assert n == "15%"


    #n = p.element_value
    #elements = pywinauto.findwindows.find_element(auto_id="MainPanelForm.ObjectEditorWidget.DefocusDetector.sbSensitivity")

    #l.find_element(auto_id="MainPanelForm.ObjectEditorWidget.DefocusDetector.sbSensitivity")
    #m = l.Value.Value
    #Value.Value:	"15%"
    #dlg.child_window(auto_id="MainPanelForm.ObjectEditorWidget.DefocusDetector.sbSensitivity").send_input("30")
    time.sleep(1)
    #dlg.Компьютер.double_click_input()
    #d = dir(dlg.Компьютер)
    #print("____________")
    #print(d)
    #print(dlg.Компьютер.dump_tree())


def test_try_to_work_with_tree_item():
    app = Application(backend="uia").connect(title='Панель управления SecurOS Enterprise')
    dlg = app.window(title='Панель управления SecurOS Enterprise')
    #dlg.child_window(title="Компьютер VQA-2 [VQA-2]", control_type="TreeItem").double_click_input()
    treeview = dlg[u'ATL:SysTreeView32']
    #treeview.select('\\Система')
    tree_item = treeview.get_item([u'\Система'])
    time.sleep(1)
    print(tree_item)

def expand_tree_to_detector(dlg):
    if dlg.child_window(title="SecurOS Enterprise [1]", control_type="TreeItem").exists():
        pass
    else:
        dlg.child_window(title="Система", control_type="TreeItem").double_click_input()
        dlg.Отмена.click_input()
    if dlg.child_window(title="Серверы и Рабочие места", control_type="TreeItem").exists():
        pass
    else:
        dlg.child_window(title="SecurOS Enterprise [1]", control_type="TreeItem").double_click_input()
        dlg.Отмена.click_input()
    if dlg.child_window(title="Компьютер VQA-2 [VQA-2]", control_type="TreeItem").exists():
        pass
    else:
        dlg.child_window(title="Серверы и Рабочие места", control_type="TreeItem").double_click_input()
    if dlg.child_window(title="Устройства (Камеры и Микрофоны)", control_type="TreeItem").exists():
        pass
    else:
        dlg.child_window(title="Компьютер VQA-2 [VQA-2]", control_type="TreeItem").double_click_input()
        dlg.Отмена.click_input()
    if dlg.child_window(title="grab 202 [202]", control_type="TreeItem").exists():
        pass
    else:
        dlg.child_window(title="Устройства (Камеры и Микрофоны)", control_type="TreeItem").double_click_input()
    if dlg.child_window(title="cam 202 [202]", control_type="TreeItem").exists():
        pass
    else:
        dlg.child_window(title="grab 202 [202]", control_type="TreeItem").double_click_input()
        dlg.Отмена.click_input()
    if dlg.child_window(title="det 202 [202]", control_type="TreeItem").exists():
        pass
    else:
        dlg.child_window(title="cam 202 [202]", control_type="TreeItem").double_click_input()
        dlg.Отмена.click_input()
    dlg.child_window(title="det 202 [202]", control_type="TreeItem").double_click_input()