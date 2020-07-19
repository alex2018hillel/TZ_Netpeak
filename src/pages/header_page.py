from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HeaderPage:
    job_button = (By.XPATH, '//*[@class="vac-block-border"]/div/a')
    driver = None


    def __init__(self, driver):
        self.driver = driver


    def at_page(self):
        return "Работа в Netpeak: обращение руководителя, видео и презентация о карьере в Нетпик Украина" in self.driver.title


    def click_job_button(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="vac-block-border"]/div/a')))
        self.driver.find_element(By.XPATH,'//*[@class="vac-block-border"]/div/a').click()


