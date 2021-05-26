import time

import autoit
import pyautogui
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\automation"
# Using an existing Chrome session
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.add_argument("--auto-open-devtools-for-tabs")
chrome_driver = r"E:\PROJECTS\princeton\chromedriver"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)

classes = ['Class Two', 'Class Three', 'Class Four', 'Class Five', 'Class Six', 'Class Seven']

link = 'https://cdn.princetonreview.com/InstructionalContent/GRE/video/sd/'
link_end = '.sml.mp4'
lis = []
data = pd.read_csv('Class One.csv')
lis = data.values.tolist()

for x in lis:
    browser.get(link + str(x[0]) + link_end)
    time.sleep(2)
    # Entered Video Page, saving the file
    pyautogui.hotkey('ctrl','s')
    pyautogui.press('enter')
    #  accepting Windows Dialog to Save file
    time.sleep(1)

    autoit.control_focus("Save As", "Edit1")
    autoit.control_set_text("Save As", "Edit1", "asd.mp4")
    autoit.control_focus("Save As", "Button2")
    pyautogui.press('enter')

    # autoit.control_c
    # lick("Save As", "Button2")
    time.sleep(10)