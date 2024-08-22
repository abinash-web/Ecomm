from selenium.webdriver.common.by import By

from PageObject.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text()='Shop']")
    # driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys("Rahul")
    name = (By.CSS_SELECTOR,"[name='name']")
    #input[class='form-control ng-touched ng-dirty ng-invalid']
    #name=(By.CSS_SELECTOR,"input[class='form-control ng-touched ng-dirty ng-invalid']")
    # driver.find_element(By.NAME, "email").send_keys("shetty")
    email = (By.NAME, "email")
    # #driver.find_element(By.ID, "exampleCheck1").click()
    checkbox = (By.ID, "exampleCheck1")
    # (By.ID, "exampleFormControlSelect1")
    select_By_male = (By.ID, "exampleFormControlSelect1")
    # By.XPATH, "//input[@value='Submit']")
    submit = (By.XPATH, "//input[@value='Submit']")
    # t(By.XPATH, "//div[@class='alert alert-success alert-dismissible']
    conform_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_select_dropdown(self):
        return self.driver.find_element(*HomePage.select_By_male)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_validation_sucess_message(self):
        return self.driver.find_element(*HomePage.conform_message)
