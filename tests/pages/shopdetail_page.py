from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

class ShopdetailPage:
    URL = "https://www.nibbuns.co.kr/shop/bestseller.html?xcode=BEST&ref=&suburl=shop%2Fbestseller.html%3Fxcode%3DBEST/"
    SEARCH_INPUT_ID = '//*[@id="hd"]/div[3]/div[1]/div[2]/form/fieldset/input'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def open_page(self, url : str):
        self.driver.get(url)

    def search_items(self, item_name : str):
        search_input_box = self.driver.find_element(By.XPATH, self.SEARCH_INPUT_ID)
        for char in item_name:
            search_input_box.send_keys(char)
            time.sleep(2)
        search_input_box.send_keys(Keys.ENTER)

    def click_by_LINK_TEST(self, like_text: str):
        login_button = self.driver.find_element(By.LINK_TEXT, like_text)
        login_button.click()