from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
cv_path = os.path.join(os.path.sep, ROOT_DIR, "CV.png")


class JobPage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    wait = WebDriverWait(driver, 10)
    text_error = "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)."

    def at_page(self):
        return "Заполнение анкеты на вакансию — Netpeak Украина" in self.driver.title


    def message(self):
        return "ERROR" in self.driver.title


    def get_random_string(self,length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str.capitalize()


    def get_random_phone(self, size=12, chars=string.digits):
        result =  ''.join(random.choice(chars) for _ in range(size))
        return ("+" + result)


    def get_random_email(self):
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(5))
        email = name +"@gmail.com"
        return email


    def send_cv_file(self):
        self.driver.implicitly_wait(10)
        inp = self.driver.find_element_by_css_selector('input[name="up_file"]')
        inp.send_keys(cv_path)
        present = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//div[@id="up_file_name"]/label'), self.text_error))
        self.error = self.driver.find_element_by_css_selector('div[id="up_file_name"]')


    def send_data(self):
        name = self.driver.find_elements_by_xpath('//input[@id="inputName"]')
        name[0].send_keys(self.get_random_string(8))

        last = self.driver.find_elements_by_xpath('//input[@id="inputLastname"]')
        last[0].send_keys(self.get_random_string(8))

        field = self.driver.find_elements_by_xpath('//input[@id="inputEmail"]')
        field[0].send_keys(self.get_random_email())

        phone = self.driver.find_elements_by_xpath('//input[@id="inputPhone"]')
        phone[0].send_keys(self.get_random_phone())

        years = self.driver.find_elements_by_xpath("//div/select/option[contains(text(),'Год')]/../option")
        for option in years:
            if option.get_attribute('value') == "2000":
                option.click()
                break

        months = self.driver.find_elements_by_xpath("//div/select/option[contains(text(),'Месяц')]/../option")
        for option in months:
            if option.get_attribute('value') == "07":
                option.click()
                break

        days = self.driver.find_elements_by_xpath("//div/select/option[contains(text(),'День')]/../option")
        for option in days:
            if option.get_attribute('value') == "02":
                option.click()
                break

        button = self.driver.find_elements_by_xpath('//button[@id="submit"]')
        button[0].click()

        warning_fields = self.driver.find_elements_by_xpath("//p[contains(text(),'Все поля являются обязательными для заполнения')]")
        self.text_color = warning_fields[0].value_of_css_property('color')


    def click_logo(self):
        self.driver.find_element(By.XPATH,'//div[@class="logo-block"]/a').click()


    def error_message(self):
        return self.text_error in self.error.text


    def color_atr(self):
        return "rgba(255, 0, 0, 1)" in self.text_color



