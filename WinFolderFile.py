import ntpath
import pywinauto
import time


def OpenWin(filePath):
    pwa_app = pywinauto.application.Application()
    time.sleep(3)
    w_handle = pywinauto.findwindows.find_windows(title='Open')[0] #, class_name='Window')[0]  ;;, visible_only=True
    try:
        pwa_app.connect(title='Open')
        window = pwa_app.window_(handle=w_handle)
        #pwa_app.
        ctrl = window['Edit']
        ctrl.SetText(filePath)  #set_edit_text
        ctrl = window['&Open']
        ctrl.Click()
    except Exception as errMsg:
        print (errMsg)


    return path_leaf(filePath)

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail     #tail is the file name, head is the base folder