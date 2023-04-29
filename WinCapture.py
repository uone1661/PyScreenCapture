import numpy as np
import win32api, win32gui, win32ui, win32con
import cv2

class CWIN:

    CWc = int(win32api.GetSystemMetrics(win32con.SM_CXSCREEN) / 2)
    
    CHc = int(win32api.GetSystemMetrics(win32con.SM_CYSCREEN) / 2)

    DWIN = win32gui.GetDesktopWindow()

# 窗口截圖
def get_win_screenshot(hwnd, rangew, rangeh):

    window_rect = win32gui.GetWindowRect(hwnd)

    win_w = window_rect[2] - window_rect[0]
    win_h = window_rect[3] - window_rect[1]

    wc = int(win_w / 2)

    hc = int(win_h / 2)

    cx = int(wc - rangew / 2)

    cy = int(hc - rangeh / 2)

    width = rangew

    height = rangeh

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (width, height), dcObj, (cx, cy), win32con.SRCCOPY)

    signedIntsArray = dataBitMap.GetBitmapBits(True)

    img = np.fromstring(signedIntsArray, dtype='uint8')

    img.shape = (width, height, 4)

    # free resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    img = img[...,:3]

    img = np.ascontiguousarray(img)

    return img

# 螢幕截圖
def get_grab_screen(rangew, rangeh):

    hwin = CWIN.DWIN

    wc = CWIN.CWc

    hc = CWIN.CHc

    left = int(wc - rangew / 2)
    top = int(hc - rangeh / 2)

    width = rangew
    height = rangeh

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height, width, 4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    img = img[...,:3]

    img = np.ascontiguousarray(img)

    return img
