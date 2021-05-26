import re
import time
# import autoit
import pyautogui
import pandas as pd
from bs4 import BeautifulSoup as soup
import lxml
import csv
import numpy as np



from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\automation"
# Using an existing Chrome session
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.add_argument("--auto-open-devtools-for-tabs")
chrome_driver = r"D:\PROJECT\princeton\chromedriver"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)


# Click on Syllabus Tab and select ClassOne
# Fetch all Folders within the class
# Iterate through Folders as Class structure
# ---- Further Iterate
browser.find_element_by_link_text('Syllabus').click()
classes = ['Class One', 'Class Two', 'Class Three', 'Class Four', 'Class Five', 'Class Six', 'Class Seven']

for class_name in classes:
    browser.find_element_by_link_text(class_name).click()
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/button[1]').click()
    time.sleep(4)
    html=browser.page_source
    soups=soup(html,'html.parser')
    tables = soups.findAll('a')
    lis = []
    for x in tables:
        lis.append(str(x))
    lis_df = pd.DataFrame(lis)
    lis_df.to_csv('list.csv')

    lis = []
    data = pd.read_csv('list.csv')
    lis = data.values.tolist()

    temp_lis = []
    for x in lis:

        if 'ga-video' in str(x) or 'ga-articulate' in str(x):
            tag = "a"
            reg_str = ">(.*?)</" + tag + ">"
            res = re.findall(reg_str, str(x))
            print(str(res[0])[10:-8])
            temp_lis.append(str(res[0])[10:-8])
    temp_df = pd.DataFrame(temp_lis)
    file_name = str(class_name) + ".csv"
    temp_df.to_csv(file_name)









# df = pd.DataFrame(table)

# lis_df = pd.DataFrame(tb)
# lis_df.to_csv('list.csv')
# for item in tb:
#     text = item.text
#     print(text)



# # Entered Video Page, saving the file
# time.sleep(5)
# pyautogui.hotkey('ctrl','s')
# pyautogui.press('enter')
#
# #  accepting Windows Dialog to Save file
# time.sleep(5)
# autoit.control_click("Save As", "Button2")
