
import pyautogui, time
f = open("spamtext", 'r')
time.sleep(5)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    
#spamtext is the file name here it contains the text to be spammed.


