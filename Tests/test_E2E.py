from selenium import webdriver
import pytest

# chrome driver
from selenium.webdriver.chrome.service import Service
# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Page_obj.CartItem import CartItem
from Page_obj.HomePage import HomePage
from utilities.BaseClass import Base


class TestShoppingCart(Base):

    def test_e2e(self):


        #  //a[contains(@href,'shop')]    a[href*='shop']
        homepageDriver = HomePage(self.driver)
        homepageDriver.shop().click()
        cartiteam = CartItem(self.driver)
        products = cartiteam.getProducts()
        cartiteam.addToCart("Blackberry")
        # for product in products:
        #     productName = product.find_element(By.XPATH, "div/h4/a").text
        #     if productName == "Blackberry":
        #         product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successText

