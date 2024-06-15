import pyautogui
import time

print('Program will running in 5 seconds')
time.sleep(5)

for i in range(0, 50):
    print("{0}".format(i))
    pyautogui.write("hey @here")
    pyautogui.press("enter")