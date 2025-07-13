import time

from pageObjects.loginPage import LoginPage
from pageObjects.Add__custmerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string
from pageObjects.screenshots import capture_screenshot
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

class Test__003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)) + "@gmail.com"


    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        try:
            self.logger.info("******** Test__003 AddCustomer ************")
            self.driver = setup
            self.driver.get(self.baseUrl)
            self.driver.maximize_window()

            self.lp = LoginPage(self.driver)
            self.lp.login_to_account(self.username, self.password)
            self.logger.info("********** Login Succesful ******************")


            self.logger.info("********** Starting Add Customer Test ******************")

            self.addcust = AddCustomer(self.driver)
            self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")

            self.addcust.clickOn_Addnew()

            email = self.random_email()
            self.addcust.setEmail(email)
            self.addcust.setPassword("test123")
            self.addcust.setfirstname("Ajay")
            self.addcust.setLastName("GV")
            self.addcust.setgender("Male")
            self.addcust.setCompanyName("OpenAI")
            self.addcust.taxextempt()
            self.addcust.setMangerofvendor("Vendor 1")
            self.addcust.customerchangedpassword()
            self.addcust.adminComment("This is a test customer created using automation.")
            self.addcust.saveCustomerdetails()

            self.logger.info("********** Customer added successfully ******************")
            time.sleep(10)
        except Exception as e:
            capture_screenshot(self.driver,"AddCustomer","test_addCustomer")
            self.logger.error(f"**** Add Customer Test Failed: Found  ****")
            assert False


        self.msg = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-success alert-dismissable']"))
        ).text

        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("Succesfull customer details Added")
            self.driver.close()

        else:
            capture_screenshot(self.driver,"Customer Succesful message","test_addCustomer")
            self.logger.info("Test Failed while Adding customer details ")
            assert False



