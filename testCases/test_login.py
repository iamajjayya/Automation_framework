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

    def test_login_details(self,setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        login = LoginPage(self.driver)
        login.login_to_account("admin@yourstore.com","admin")







