from selenium.webdriver.common.by import By

from PageObject.ConfirmPage import ConfirmPage


class CheckoutPage:
    # self.driver.find_elements(By.XPATH, "//div[@class='card h-100']"
    # self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    checkout = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def checkoutItem(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
