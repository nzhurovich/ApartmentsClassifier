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




class WebDriver:
    PATH = r"C:\Program Files (x86)\chromedriver.exe"

    def __init__(self, link, PATH=PATH):
        self.PATH = PATH
        self.driver = webdriver.Chrome(PATH)
        self.link= link
        global platform
        platform = self.link

    def sleeper(self):
        randomizer = np.random.randint(3, 13)
        time.sleep(randomizer)

    def getter(self):
        self.driver.get(self.link)

class Settings():
    
    def __init__(self, rooms=1, price_min=200, price_max=99999, cooker=1, fridge=1, washer=1, tv=2, wifi=1, balcony=2):
        self.rooms = rooms
        self.price_min = price_min
        self.price_max = price_max
        self.cooker = cooker
        self.fridge = fridge
        self.washer = washer
        self.tv = tv
        self.wifi = wifi
        self.balcony = balcony


class Kufar(Settings):
    appa_links = []
    curr_page = 0
    page_nums = None
    link = "https://re.kufar.by"
    driver = WebDriver(link)
    driver.getter()

    def __init__(self):
        super().__init__(Settings)

    def get_appa_links(self):
        pass

    def get_page_nums(self):
        pass
    
    def go_next_page(self):
        pass


class Appa:
    pass


class image_processor:
    pass

