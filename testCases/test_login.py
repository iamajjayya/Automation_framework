import pytest

from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.screenshots import capture_screenshot


class TestLogin:
    baseurl = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUsername()
    passWord = ReadConfig.getPassword()


    @pytest.mark.regression
    def test_login_title(self, setup):
        logger = LogGen.loggen()
        logger.info("**** Test Case: test_login_title ****")
        logger.info("**** Verifying Home Page Title ****")

        self.driver = setup
        self.driver.get(self.baseurl)
        actual_title = self.driver.title

        if actual_title == "nopCommerce demo store. Login":
            logger.info("**** Home Page Title Test Passed ****")
            self.driver.close()
            assert True
        else:
            capture_screenshot(self.driver, "Test_Login_Title", "test_login.py")
            logger.error(f"**** Home Page Title Test Failed: Found '{actual_title}' ****")
            self.driver.close()
            assert False
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login_with_valid_data(self, setup):
        logger = LogGen.loggen()
        logger.info("**** Test Case: test_login_with_valid_data ****")
        logger.info("**** Logging in with Valid Credentials ****")

        self.driver = setup
        self.driver.get(self.baseurl)

        login = LoginPage(self.driver)
        login.login_to_account(self.userName, self.passWord)

        logger.info("**** Login attempt completed ****")
        self.driver.close()
