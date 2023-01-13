import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFF
from selenium.webdriver.safari.service import Service as ServiceSafari


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browserName = request.config.getoption("--browser_name")
    if browserName == "chrome":
        service_obj = ServiceChrome("/Users/khushbutiwari/Documents/Selenium_Doc/Software/Chrome/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    if browserName == "firefox":
        service_obj = ServiceFF("/Users/khushbutiwari/Documents/Selenium_Doc/Software/FF/geckodriver")
        driver = webdriver.Chrome(service=service_obj)
    if browserName == "safari":
        service_obj = ServiceSafari("/usr/bin/safaridriver")
        driver = webdriver.Safari(service=service_obj)
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
