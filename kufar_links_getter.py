from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import pandas as pd
import numpy as np

link = 'https://re.kufar.by/l/minsk/snyat/kvartiru-dolgosrochno'
PATH = r"C:\Program Files (x86)\chromedriver.exe"
appa_links = []
curr_page = 0
page_nums = None


def setup(link, price_min=200, price_max=9000, rooms=1):
    link += "/{}k?cur=USD".format(rooms)
    link += "&prc=r%3A{}%2C{}".format(price_min, price_max)
    return link

def list_to_dict(d, l):
    for i in l:
        key, value = i[0], i[1]
        d[key] = value
    return d

driver = webdriver.Chrome(PATH)
driver.get(setup(link))
time.sleep(7)
page_nums = driver.find_elements_by_class_name('kre-bfYs-a2a66')
page_nums = int(page_nums[-2].text)

for page in range(page_nums-1):
    time.sleep(np.random.randint(3, 7))
    hrefs = []
    for elem in driver.find_elements_by_tag_name('a'):
        href = elem.get_attribute('href')
        if href is not None and 'https://re.kufar.by/vi/minsk/snyat/kvartiru-dolgosrochno/' in href: 
            appa_links.append([href.split('/')[-1], href])
            #print(href)
        if href is not None and '/listings?cat=' in href:
            hrefs.append(href)
    time.sleep(8)
    print('there are {} pages scrapped!'.format(page))
    driver.get(hrefs[-1])

data = pd.DataFrame(appa_links, columns = ['appa_num', 'href'])
data.to_csv('kufar.csv')
