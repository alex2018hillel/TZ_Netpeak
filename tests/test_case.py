import pytest
from selenium import webdriver
from src.pages.header_page import HeaderPage
from src.pages.netpeak import NetpeakPage
from src.pages.job_page import JobPage


# DRIVER_PATH = "bin/chromedriver"
DRIVER_PATH = "/home/circleci/repo/bin/chromedriver"


class TestResourse:
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        self.netpeak = NetpeakPage(self.driver)
        self.header_page = HeaderPage(self.driver)
        self.job_page = JobPage(self.driver)


    def test_career(self):
        self.netpeak.open()
        assert self.netpeak.at_page()
        self.netpeak.click_career_button()
        assert self.header_page.at_page()
        self.header_page.click_job_button()
        self.job_page.send_cv_file()
        assert self.job_page.error_message()

        self.job_page.send_data()
        assert self.job_page.color_atr()

        self.job_page.click_logo()
        assert self.netpeak.at_page()


    def teardown_method(self):
        self.driver.close()


if __name__ == "__main__":
    pytest.main()

