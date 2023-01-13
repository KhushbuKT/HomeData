from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePageFormObj:
    name = (By.XPATH, "(//input[@name='name'])[1]")
    email = (By.XPATH, "(//input[@name='email'])[1]")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    submit = (By.CSS_SELECTOR, "input.btn")
    suceesText = (By.CSS_SELECTOR, "div.alert")

    def __init__(self, driver):
        self.driver = driver

    def setName(self):
        return self.driver.find_element(*HomePageFormObj.name)

    def setEmail(self):
        return self.driver.find_element(*HomePageFormObj.email)

    def setPassword(self):
        return self.driver.find_element(*HomePageFormObj.password)

    def setGender(self, gender):
        sel = Select(self.driver.find_element(*HomePageFormObj.gender))
        sel.select_by_visible_text(gender)

    def getSuccessText(self):
        return self.driver.find_element(*HomePageFormObj.suceesText)

    def setSubmit(self):
        return self.driver.find_element(*HomePageFormObj.submit)

