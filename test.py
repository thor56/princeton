import time
import autoit
import pyautogui

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\automation"

# Using an existing Chrome session
chrome_options = Options()


chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.add_argument("--auto-open-devtools-for-tabs")

chrome_driver = r"E:\PROJECTS\princeton\chromedriver"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)

time.sleep(5)
pyautogui.hotkey('ctrl','s')
pyautogui.press('enter')

time.sleep(5)
autoit.control_click("Save As", "Button2")
