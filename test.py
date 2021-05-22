import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pyautogui
from selenium.webdriver.common.keys import Keys

link = "https://startblogging.co/affiliate-product-table-generator"

# Using an existing Chrome session
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.add_argument("--auto-open-devtools-for-tabs")
chrome_options.


chrome_driver = r"E:\NOTES\princeton\chromedriver"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)

# browser.get(link)
# use url syntax and change name of the video file to get to the video page
# browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL, 's')
# browser.find
time.sleep(5)
pyautogui.hotkey('ctrl','s')
pyautogui.press('enter')



