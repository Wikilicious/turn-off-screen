#!/usr/bin/env python
import win32gui
import win32con
from os import getpid, system
from threading import Timer

def force_exit():
    pid = getpid()
    system('taskkill /pid %s /f' % pid)

t = Timer(1, force_exit)
t.start()
SC_MONITORPOWER = 0xF170
win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2)
t.cancel()