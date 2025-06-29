import pytest


from pageObjects.loginPage import LoginPage


class TestLogin:
    def test_login_title(self, setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        actual_title = self.driver.title
        if actual_title == "nopCommerce demo store. Login":
            assert True
        else:
            assert False
        self.driver.close()

    def test_login_with_valid_data(self,setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        login = LoginPage(self.driver)
        login.login_to_account("admin@yourstore.com","admin")
        self.driver.close()

    def test_login_with_invalid_email_id(self,setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        login  = LoginPage(self.driver)
        login.login_to_account("admiourstore.com","admin")
        actual_msg = login.get_email_error_msg()
        assert  "Please enter a valid email address." in actual_msg
        self.driver.close()

    def test_login_invalid(self,setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        login = LoginPage(self.driver)
        login.login_to_account("admin@yourstore.com","admin123")
        actual_msg = login.get_error_validation()
        print(actual_msg)

        self.driver.close()










