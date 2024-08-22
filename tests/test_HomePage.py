import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.Homepage import HomePage
from utility.BaseOne import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmition(self, getData):
        log = self.test_logger()
        log.info(("first name is"+getData["Firstname"]))
        # service_obj = Service()
        # driver = webdriver.Chrome(service=service_obj)
        # # driver.implicitly_wait(5)
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        # driver.maximize_window()

        # driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys("Rahul")

        homepage = HomePage(self.driver)
        # homepage.getName().send_keys(getData[0])
        homepage.getName().send_keys(getData["Firstname"])

        # homepage.getName().send_keys("Rahul")
        # driver.find_element(By.NAME, "email").send_keys("shetty")
        # homepage.getEmail().send_keys(getData[1])
        homepage.getEmail().send_keys(getData["Lastname"])
        # homepage.getEmail().send_keys("shetty")
        # driver.find_element(By.ID, "exampleCheck1").click()
        homepage.getcheckbox().click()

        # sel = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # sel = Select(homepage.get_select_dropdown())
        # sel.select_by_visible_text("Male")
        # self.SelectOptionByText(homepage.get_select_dropdown(), getData[2])
        self.SelectOptionByText(homepage.get_select_dropdown(), getData["Gender"])
        # self.SelectOptionByText(homepage.get_select_dropdown(), "Male")
        # driver.find_element(By.XPATH, "//input[@value='Submit']").click()
        homepage.get_submit().click()

        # alert_text = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        alert_text = homepage.get_validation_sucess_message().text
        assert "success" in alert_text
        self.driver.refresh()

    # list format
    # @pytest.fixture(params=[("Rahul", "shetty", "Male"), ("Anshika", "shetty", "Female")])
    # def getData(self, request):
    #     return request.param
    # Dictinary format
    @pytest.fixture(params=[{"Firstname":"Rahul","Lastname":"shetty","Gender":"Male"},{"Firstname":"Anshika", "Lastname":"shetty","Gender":"Female"}])
    def getData(self, request):

        return request.param

    # @pytest.fixture(params=HomePageData.test_HomePage_DataStore)
    # def getData(self,request):
    #     return request.param

