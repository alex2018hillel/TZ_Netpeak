from selenium.webdriver.common.by import By


class HeaderPage:
    job_button = (By.XPATH, '//*[@class="vac-block-border"]/div/a')
    driver = None


    def __init__(self, driver):
        self.driver = driver


    def at_page(self):
        return "Работа в Netpeak: обращение руководителя, видео и презентация о карьере в Нетпик Украина" in self.driver.title


    def click_job_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,'//*[@class="vac-block-border"]/div/a').click()


