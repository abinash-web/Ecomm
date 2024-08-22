import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from PageObject.CheckoutPage import CheckoutPage
from PageObject.Homepage import HomePage
from utility.BaseOne import BaseClass


# @pytest.mark.use fixtures("setup")

class TestOne(BaseClass):
    def test_e2e(self):
        log=self.test_logger()
        homepage = HomePage(self.driver)
        # homepage.shopItem().click()
        checkoutpage = homepage.shopItem()

        # self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
        # list_of_product = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        checkoutPage = CheckoutPage(self.driver)

        list_of_product = checkoutpage.getCardTitles()

        for product in list_of_product:
            product_item = product.find_element(By.XPATH, "div/h4/a").text
            log.info(product_item)
            if product_item == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        #checkoutpage.checkoutItem().click()

        confirm_page = checkoutpage.checkoutItem()
        log.info("enter country name as in  Ind")

        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        #calling from Base class using utilities package
        self.verifyLinkprensce("India")

        self.driver.find_element(By.XPATH, "//a[text()='India']").click()
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        sucess = self.driver.find_element(By.CLASS_NAME, 'alert-success').text
        print(sucess)
        log.info("text recived from application is "+sucess)
        assert "Success! Thank you12345! Your order will be delivered in next few weeks" in sucess
