import pyautogui
import time

def AutoOpen():
    win_position = (16, 1051) #滑鼠需要移動的位置
    pyautogui.moveTo(win_position) #控制滑鼠移動
    pyautogui.click(clicks=1) #實現滑鼠單擊
    time.sleep(1)

    down_position = (388, 1020)
    pyautogui.moveTo(down_position) #控制滑鼠移動
    pyautogui.click(clicks=109) #實現滑鼠單擊
    time.sleep(1)

    safe_position = (200, 995)
    pyautogui.moveTo(safe_position) #控制滑鼠移動
    pyautogui.click(clicks=1) #實現滑鼠單擊
    time.sleep(1)

if __name__ == '__main__':
 AutoOpen()