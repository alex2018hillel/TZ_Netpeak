import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from src.pages.header_page import HeaderPage
from src.pages.netpeak import NetpeakPage
import allure


url = "https://netpeak.ua"

# class Driver:
#     def __init__(self):
#         options = Options()
#         # options.headless = True
#         options.headless = False
#         self.driver = webdriver.Firefox(options=options)


class TestResourse:
    def setup_method(self):
        options = Options()
        # options.headless = True
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        # self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.netpeak = NetpeakPage(self.driver)
        self.header_page = HeaderPage(self.driver)

    # @allure.step
    # def test_open_url(self):
    #     options = Options()
    #     # options.headless = True
    #     options.headless = False
    #     # self.driver = webdriver.Firefox(executable_path=ChromeDriverManager().install())
    #     #
    #     self.driver = webdriver.Firefox(options=options)
    #     self.driver.get(url)
    #     assert "Раскрутка сайта, продвижение сайтов: Netpeak Украина — performance-маркетинг для бизнеса" in self.driver.title
    #     # assert "Работа в Netpeak: обращение руководителя, видео и презентация о карьере в Нетпик Украина" in self.driver.title


    # @allure.title("Netpeak")
    @allure.feature("Open Netpeak page")
    # @allure.story("Page career")
    # @pytest.mark.uipy
    def test_career(self):
        self.netpeak.open()
        assert self.netpeak.at_page()
        self.netpeak.click_career_button()
        assert self.header_page.at_page()

        # self.netpeak.click_career_button()
        # with allure.step("at_page"):
        #     assert self.header_page.at_page()

        # self.login_page.open()
        # assert self.login_page.at_page()
        # self.login_page.login_to_jira()
        # assert self.header_page.at_page()


    def teardown_method(self):
        self.driver.close()

    # class LoginPage:
    #     LOGIN_INPUT = (By.ID, "login-form-username")
    #     PASSWORD_INPUT = (By.ID, "login-form-password")
    #     LOGIN_BUTTON = (By.ID, "login")
    #     driver = None
    #
    #     def __init__(self, driver):
    #         self.driver = driver
    #
    #     @allure.step
    #     def login_to_jira(self):
    #         self.driver.find_element(*self.LOGIN_INPUT).clear()
    #         self.driver.find_element(*self.LOGIN_INPUT).send_keys("webinar5")
    #         self.driver.find_element(*self.PASSWORD_INPUT).clear()
    #         self.driver.find_element(*self.PASSWORD_INPUT).send_keys("webinar5")
    #         self.driver.find_element(*self.LOGIN_BUTTON).submit()
    #
    #     # Login to mailbox form
    #     def test_first(self):
    #         global action, theme, text, create_email
    #         wdriver = self.driver
    #         parser = configparser.ConfigParser()
    #         parser.read('simple_config.ini')
    #         url = parser.get('data', 'url')
    #         user_name = parser.get('data', 'username')
    #         password = parser.get('data', 'password')
    #         wdriver.get(url)
    #         login_field = wdriver.find_element_by_xpath(Login_page.login_field)
    #         login_field.send_keys(user_name)
    #         password_field = wdriver.find_element_by_xpath(Login_page.password_field)
    #         password_field.send_keys(password)
    #         button_login = wdriver.find_element_by_xpath(Login_page.button_login)
    #         button_login.click()





# class TestLogin:
#
#     def test_login_to_jira(self):
#         driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get("http://jira.hillel.it:8080/secure/Dashboard.jspa")
#         assert "System Dashboard - Hillel IT School JIRA" in driver.title