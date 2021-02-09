import pyautogui
import time

x, y = pyautogui.position()
pyautogui.click(88, 1052, button="left")
time.sleep(0.1)
pyautogui.write("camera privacy settings")
time.sleep(0.1)
pyautogui.click(288, 369, button="left")
time.sleep(0.5)
pyautogui.click(580, 600, button="left")
time.sleep(0.1)
pyautogui.click(1352, 35, button="left")
pyautogui.moveTo(x,y)
