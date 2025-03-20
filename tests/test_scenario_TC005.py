import pytest
import os
import time
import logging
from selenium import webdriver
from pages.main_Bini import InquiryPage


log_file = os.path.join(os.getcwd(), "test_scenario_TC005.log")

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filename = log_file,
    encoding="utf-8",
    filemode = 'a',
    force=True
)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def inquiry_page(driver):
    return InquiryPage(driver)



# test1. 문의페이지 글쓰기 페이지 이동
def test_PAGE_MOVE(inquiry_page):
    logger.info("[Test1.] 테스트 시작")
    inquiry_page.OPEN_INQUIRIES_PAGE("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    current_url = inquiry_page.driver.current_url
    logger.info(f"✅현재 URL : {current_url}")
    assert "nibbuns.co.kr/board/board.html" in current_url, "❌ 페이지 이동 실패"
    time.sleep(1)
    inquiry_page.CLICK_WRITING_BUTTON()
    current_url = inquiry_page.driver.current_url
    #logger.info("'글쓰기' 페이지 이동중..")
    logger.info(f"✅현재 URL : {current_url}")

