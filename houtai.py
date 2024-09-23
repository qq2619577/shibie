import win32gui, win32con,win32api,time

def send_mouse(hwnd,x,y):
    #鼠标移动到指定位置
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0,(y<<16)| x)
    #鼠标左键按下
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, (y<<16)| x)
    time.sleep(0.1)
    #鼠标左键弹起
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, (y<<16)| x)
    time.sleep(0.1)

def find_window(title,son_title):
    #查找窗口
    fa_hwnd = win32gui.FindWindow(None, title)
    if fa_hwnd:
        hwnd = win32gui.FindWindowEx(fa_hwnd, None,None,son_title)
        print(hwnd)
        print(fa_hwnd)
    return hwnd


def main():
    hwnd = find_window("MuMu模拟器12","MuMuPlayer")
    if hwnd:
        send_mouse(hwnd, 800,168)
        print("鼠标左键点击成功")

if __name__ == '__main__':
    main()