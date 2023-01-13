# self.driver.find_element(By.CSS_SELECTOR," a[href*='shop']").click()
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shopele = (By.CSS_SELECTOR, "a[href*='shop']")

    # product.find_element(By.XPATH, "div/h4/a")

    def shop(self):
        return self.driver.find_element(*HomePage.shopele)
