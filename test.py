import time
import autoit
import pyautogui
import pandas as pd
from bs4 import BeautifulSoup as soup
import lxml



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
classes = pd.read_csv("undersyllabus.csv")
browser.find_element_by_link_text('Class Four').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/button[1]').click()
time.sleep(4)
html=browser.page_source
soups=soup(html,'html.parser')
tables = soups.findAll('a')
lis = []

# for table in tables:
#      if table.findParent("table") is None:
lis.append(tables)
for item in tables:
    text = item.text
    print(text)



lis_df = pd.DataFrame(lis)
lis_df.to_csv('list.csv')



# tb = browser.find_elements_by_tag_name('td')
# html=browser.page_source
# soups=soup(html,'html.parser')
# div=soups.select_one("div#collapseSpecs")
# table=pd.read_html(str(div))
# print(table[0])
# print(table[1])


# df = pd.DataFrame(table)

# lis_df = pd.DataFrame(tb)
# lis_df.to_csv('list.csv')
# for item in tb:
#     text = item.text
#     print(text)


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
