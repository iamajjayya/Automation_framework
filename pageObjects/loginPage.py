from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage(BasePage):
    Username_input = (By.ID,"Email")
    Password_input = (By.ID,"Password")
    Login_button = (By.CSS_SELECTOR,"button[type='submit']")
    link_logout= (By.LINK_TEXT,"Logout")


    def login_to_account (self, username,password,timeout=10):
        try:
            email_filed = WebDriverWait(self.driver,timeout,poll_frequency=0.5).until(EC.visibility_of_element_located(self.Username_input))
            email_filed.clear()
            email_filed.send_keys(username)

            password_filed = WebDriverWait(self.driver,timeout,poll_frequency=0.5).until(
                EC.visibility_of_element_located(self.Password_input)
            )
            password_filed.click()
            password_filed.send_keys(password)

            login_button = WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(EC.visibility_of_element_located(self.Login_button))
            login_button.click()

        except TimeoutException:
            print("Login Page : Timeout during Login Interaction")
            raise




