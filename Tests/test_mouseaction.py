import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/khushbutiwari/Documents/Selenium_Doc/Software/Chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert= driver.switch_to.alert
print(alert.text)
alert.accept()
#driver.switch_to.alert.dismiss()
#driver.switchTo(). defaultContent()
# driver.find_element(By.ID,"opentab").click()
driver.execute_script("scrollBy(500, 500)")
time.sleep(4)

