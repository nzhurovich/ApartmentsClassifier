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
import os
from urllib.request import urlretrieve

PATH = r"C:\Program Files (x86)\chromedriver.exe"
links = pd.read_csv('kufar.csv')['href']
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(PATH, chrome_options=options)
appa_data = []
counter = links[-100:].shape[0]
print(counter)
def get_appa_name(link): return link.split('/')[-1]


appas_desc = []

for link in links[-100:]:
    driver.get(link)
    time.sleep(np.random.randint(5, 15))
    if not os.path.exists(r'.\images\{}'.format(get_appa_name(link))):
        os.mkdir(r'.\images\{}'.format(get_appa_name(link)))

    appa_data = {}
    appa_data['id'] = get_appa_name(link)

    raw_data = driver.find_elements_by_class_name('kre-egxM-025a6')
    for i in range(len(raw_data)):
        temp = raw_data[i].text.split('\n')
        appa_data[temp[0]] = temp[1]
    try:
        appa_data['Адрес'] = driver.find_element_by_class_name('kre-ZjSQ-b9025').text
        appa_data['Стоимость'] = driver.find_element_by_class_name('kre-ZGsF-bb961').text
        print('data parsed!')
    except:
        continue
    
    appas_desc.append(appa_data)
    images = driver.find_elements_by_tag_name('img')
    for i in range(len(images)):
        img = images[i].get_attribute('src')
        try:
            if '//yams.kufar.by/api' in img:
                path = get_appa_name(link)
                urlretrieve(img, r".\images\{}\{}_{}.png".format(path, path, i))
        except:
            pass
    
    counter -= 1 
    print('There are {} to go!'.format(counter))
    rand_time = np.random.randint(5, 17)
    time.sleep(rand_time)


pd.DataFrame(appas_desc).to_csv('appas_description_missed.csv')
