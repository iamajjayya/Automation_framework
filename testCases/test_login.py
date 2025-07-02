import pytest


from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLogin:
    baseurl = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUsername()
    passWord = ReadConfig.getPassword()

    logger  = LogGen.loggen()



    def test_login_title(self, setup):
        self.logger.info("****Test case ********")
        self.logger.info("****Verifying Home Page ******")

        self.driver = setup
        self.driver.get(self.baseurl)
        actual_title = self.driver.title
        if actual_title == "nopCommerce demo store. Login":
            self.driver.close()
            self.logger.info("**** Home Page title test is Passed  ******")
            assert True

        else:
            self.logger.info("**** Home Page title test is Failed ******")

            self.driver.close()
            assert False


    def test_login_with_valid_data(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        login = LoginPage(self.driver)
        login.login_to_account(self.userName,self.passWord)
        self.driver.close()

    def test_login_with_invalid_email_id(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        login  = LoginPage(self.driver)
        login.login_to_account(self.userName,self.passWord)
        actual_msg = login.get_email_error_msg()
        assert  "Please enter a valid email address." in actual_msg
        self.driver.close()

    def test_login_invalid(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        login = LoginPage(self.driver)
        login.login_to_account(self.userName,self.passWord)
        actual_msg = login.get_error_validation()
        print(actual_msg)

        self.driver.close()










