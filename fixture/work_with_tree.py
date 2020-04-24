from pywinauto.application import Application


def check_dlg_properties(dlg):
    p = dlg.child_window(auto_id="MainPanelForm.ObjectEditorWidget.DefocusDetector.sbSensitivity")
    v = p.legacy_properties()['Value']
    assert v == "15%"
    p1 = dlg.child_window(auto_id="MainPanelForm.ObjectEditorWidget.DefocusDetector.sbCheckTime")
    v1 = p1.legacy_properties()['Value']
    assert v1 == "2 с"
    p2 = dlg.child_window(auto_id="MainPanelForm.ObjectEditorWidget.DefocusDetector.cbCameraShiftDetect")
    v2 = p2.get_toggle_state()
    assert v2 == 0


def expand_tree_to_detector():
    app = Application(backend="uia").connect(title='Панель управления SecurOS Enterprise')
    dlg = app.window(title='Панель управления SecurOS Enterprise')
    dlg.child_window(auto_id="MainPanelForm.gridLayoutWidget.MainPanelWidget.rightFrame.setupWidget.setupButton").click()

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
    return dlg

