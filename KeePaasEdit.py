# Edit all http to https on KeePaasXC
# before Run this Search "http:" then click first data

import pyautogui
from time import sleep

pyautogui.hotkey("command", "tab")
for i in range(10):
    pyautogui.press("enter")
    pyautogui.press("tab", presses=3)
    pyautogui.press("left")
    pyautogui.press("right", presses=4)
    pyautogui.press("s")
    # print(pyautogui.position)で計測
    pyautogui.click(x=1226, y=806)
    sleep(1)
    pyautogui.press("down")
    sleep(1)

print("DONE")
