import allure
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

url = "https://netpeak.ua"

class NetpeakPage:
    career_button = (By.XPATH, '//*[@id="main-menu"]/ul/li[@class="blog"]')
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    @allure.step
    def open(self):
        self.driver.get(url)
        return self

    @allure.step
    def click_career_button(self):
        # self.driver.find_element(By.XPATH,'//*[@id="main-menu"]/ul/li[@class="blog"]').click()
        # self.find_element_by_xpath(self.career_button).click()
        # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, '//*[@id="main-menu"]/ul/li[@class="blog"]')).click()
        self.driver.find_element(By.XPATH,'//*[@id="main-menu"]/ul/li[@class="blog"]').click()

    def at_page(self):
        return "Раскрутка сайта, продвижение сайтов: Netpeak Украина — performance-маркетинг для бизнеса" in self.driver.title

