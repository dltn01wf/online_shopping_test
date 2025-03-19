from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
import random

class ShopdetailPage:
    URL = "https://www.nibbuns.co.kr/shop/bestseller.html?xcode=BEST&ref=&suburl=shop%2Fbestseller.html%3Fxcode%3DBEST/"
    SEARCH_INPUT_ID = '//*[@id="hd"]/div[3]/div[1]/div[2]/form/fieldset/input'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def open_page(self, url : str):
        self.driver.get(url)

    def all_click_by_bestiem(self):
        #link= self.driver.find_elements(By.XPATH,'//*[@id="prdBrand"]/div[3]/div/ul//a[@href]')
        links=self.driver.find_elements(By.CLASS_NAME ,"prdImg")
        print(len(links))
        for i in links :
            self.driver.execute_script("arguments[0].click();", i)
            self.driver.back()
            time.sleep(0.5)
        '''for index, j in enumerate(links) :
            print("456")
            if index % 2 ==1:
                print("789")
                self.driver.execute_script("arguments[0].click();", links[select])
                #self.driver.back()'''
        

    def choice_click_by_bestiem(self, select : int) :
        #find_elements(By.XPATH, './/a[@href]')
        links=self.driver.find_elements(By.CLASS_NAME ,"prdImg")
        self.driver.execute_script("arguments[0].click();", links[select])

    def random_click_by_bestiem(self) :
        #find_elements(By.XPATH, './/a[@href]')
        links=self.driver.find_elements(By.CLASS_NAME ,"prdImg")
        self.driver.execute_script("arguments[0].click();", links[random.randint(0, len(links)-1)])