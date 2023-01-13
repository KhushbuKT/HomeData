from selenium.webdriver.common.by import By


class CartItem:
    productsele = (By.XPATH, "//div[@class='card h-100']")
    product_name_ele = (By.XPATH, "div/h4/a")
    add_to_cart_btn_ele = (By.XPATH, "div/button")

    def __init__(self, driver):
        self.driver = driver

    def getProducts(self):
        return self.driver.find_elements(*CartItem.productsele)

    def getProduct(self):
        return self.driver.find_element(*CartItem.product_name_ele)

    def addToCart(self, product_Name):
        products = CartItem.getProducts(self)
        for product in products:
            productName = product.find_element(*CartItem.product_name_ele).text
            if productName == product_Name:
                product.find_element(*CartItem.add_to_cart_btn_ele).click()
