from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmOrder:
    def __init__(self, driver):
        self.driver = driver

    checkout_btn_ele = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    btn2_ele = (By.XPATH, "//button[@class='btn btn-success']")
    sel_country_ele = (By.ID, "country")

    def checkout(self):
        self.driver.find_element(*ConfirmOrder.checkout_btn_ele)

    def checkout2(self):
        self.driver.find_element(*ConfirmOrder.btn2_ele)

    def select_country(self, country_pre):
        self.driver.find_element(By.ID, "country").send_keys(country_pre)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        return successText

    # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    # self.driver.find_element(By.ID, "country").send_keys("ind")
    # wait = WebDriverWait(self.driver, 10)
    # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    # self.driver.find_element(By.LINK_TEXT, "India").click()
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    # successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
