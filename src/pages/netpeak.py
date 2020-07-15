from selenium.webdriver.common.by import By


url = "https://netpeak.ua"

class NetpeakPage:
    career_button = (By.XPATH, '//*[@id="main-menu"]/ul/li[@class="blog"]')
    driver = None

    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get(url)
        return self


    def click_career_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,'//*[@id="main-menu"]/ul/li[@class="blog"]').click()


    def at_page(self):
        return "Раскрутка сайта, продвижение сайтов: Netpeak Украина — performance-маркетинг для бизнеса" in self.driver.title


