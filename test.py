import WinCapture
import win32api, win32gui, win32ui, win32con
import cv2
import time

loop_time = 0

# 窗口截圖比桌面截圖速度更快。
# 備註: 特戰英豪只能用桌面截圖模式因其窗口設有保護。

while True:

    # 1.桌面截圖(中心點延伸寬高)
    img = WinCapture.get_grab_screen(200, 200)

    # 2.窗口截圖(窗口hwnd, 中心點延伸寬高)
    # hwnd = win32gui.FindWindow(None, "工作管理員") # 截圖 "工作管理員" 窗口
    # img = WinCapture.get_win_screenshot(hwnd, 200, 200)

    fps = str("FPS: " + format(round(1 / (time.time() - loop_time))))
    loop_time = time.time()
    print(fps) # 打印fps

    # 可註釋以下顯示代碼，觀察最直觀的截圖FPS
    cv2.imshow("OutPut", img)
    cv2.waitKey(1)