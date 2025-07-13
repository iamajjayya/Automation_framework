import time
import pytest


from pageObjects.loginPage import LoginPage
from pageObjects.Add__custmerPage import AddCustomer
from pageObjects.SearchExistingCustomer import search_existingcustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.screenshots import capture_screenshot
class Test_searchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerbyEmail(self,setup):
        self.logger.info("**** Search CustomerByEmail **** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.login_to_account(self.username,self.password)
        self.logger.info("*** Login succesful ***")

        self.logger.info("*** Starting search customer By email ***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuitems()

        self.logger.info("*** Searching customer by emailID ***")

        try:
            searchcust = search_existingcustomer(self.driver)
            searchcust.setByemail("steve_gates@nopCommerce.com	")
            searchcust.clickSearch()
            time.sleep(5)
            status = searchcust.searchCustomerByEmail("steve_gates@nopCommerce.com")
            assert status is True
            self.logger.info("*** Search by customer email test passed ***")


        except Exception as e:
            capture_screenshot(self.driver,"searchByemail","searchCustomer")
            self.logger.info(f"*** Search by customer email test failed: {str(e)} ***")
            assert False

        finally:
            self.driver.close()

