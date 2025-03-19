import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from urllib import parse
from pages.shopdetail_page import ShopdetailPage

@pytest.mark.usefixtures("driver")
class TestMainPage:

    def test_TC010(self, driver: WebDriver):
        try:
            Shopdetail_page = ShopdetailPage(driver)

            Shopdetail_page.open()
            time.sleep(10)
        
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("bestseller"))
            assert "bestseller" in driver.current_url
            Shopdetail_page.random_click_by_bestiem()
            time.sleep(10)
            
        except NoSuchElementException as e:
            assert False


