import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from src.pages.netpeak import NetpeakPage
from src.pages.header_page import HeaderPage
from src.pages.job_page import JobPage
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

@pytest.fixture
def driver(request):
    chrome_driver = WebDriver(executable_path='chromedriver', chrome_options=chrome_options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.close()


def test_career(driver: WebDriver):
    netpeak = NetpeakPage(driver)
    header_page = HeaderPage(driver)
    netpeak.open()
    assert netpeak.at_page()
    netpeak.click_career_button()
    assert header_page.at_page()


def test_send_cv_file(driver: WebDriver):
    netpeak = NetpeakPage(driver)
    header_page = HeaderPage(driver)
    job_page = JobPage(driver)
    netpeak.open()
    assert netpeak.at_page()
    netpeak.click_career_button()
    assert header_page.at_page()
    header_page.click_job_button()
    job_page.send_cv_file()
    assert job_page.error_message()


def test_color_atr(driver: WebDriver):
    netpeak = NetpeakPage(driver)
    header_page = HeaderPage(driver)
    job_page = JobPage(driver)
    netpeak.open()
    assert netpeak.at_page()
    netpeak.click_career_button()
    assert header_page.at_page()
    header_page.click_job_button()
    job_page.send_data()
    assert job_page.color_atr()


def test_logo(driver: WebDriver):
    netpeak = NetpeakPage(driver)
    header_page = HeaderPage(driver)
    job_page = JobPage(driver)
    netpeak.open()
    assert netpeak.at_page()
    netpeak.click_career_button()
    assert header_page.at_page()
    job_page.click_logo()
    assert netpeak.at_page()