import time
import autoit
import pyautogui

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\automation"

# Using an existing Chrome session
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.add_argument("--auto-open-devtools-for-tabs")
chrome_driver = r"E:\PROJECTS\princeton\chromedriver"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)


# Click on Syllabus Tab and select ClassOne
# Fetch all Folders within the class
# Iterate through Folders as Class structure
# ---- Further Iterate
browser.find_element_by_link_text('Syllabus').click()


#        Fetch all Video file name from the lesson names
#        Iterate through the folders as the Lessons
#        ---- Further Iterate -----
#               Open each video link and save the video(2 step process)
#

# # Entered Video Page, saving the file
# time.sleep(5)
# pyautogui.hotkey('ctrl','s')
# pyautogui.press('enter')
#
# #  accepting Windows Dialog to Save file
# time.sleep(5)
# autoit.control_click("Save As", "Button2")
