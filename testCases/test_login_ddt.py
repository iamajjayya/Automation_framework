import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v135.indexed_db import clear_object_store
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.screenshots import capture_screenshot
from utilities import ExcelUtils


class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"TestData","login.xlsx")

    def test_login_with_valid_data(self,setup):
        self.driver = setup
        logger = LogGen.loggen()
        logger.info("========== DDT Login Test Started ==========")
        self.driver.get(self.baseUrl)


        login = LoginPage(self.driver)
        rows = ExcelUtils.getRowCount(self.path,'Sheet1')
        logger.info(f"Total data rows (excluding header): {rows - 1}")


        test_statuses  = []

        for r in range(2,rows + 1):
            username = ExcelUtils.readData(self.path,'Sheet1',r,1).strip()
            password = ExcelUtils.readData(self.path,'Sheet1',r,2).strip()
            expected_result = ExcelUtils.readData(self.path,'Sheet1',r,3).strip()

            if not username:
                username = "admin@yourstore.com"

            logger.info(f"\n--- Row {r} ---")
            logger.info(f"Input :  Usernmae = {username} Password = {password} Expected Result  = {expected_result} ")

            login.login_to_account(username, password)
            time.sleep(2)

            actual_title = self.driver.title
            expected_title  = "Dashboard / nopCommerce administration"
            logger.info(f"Actual Page Title : {actual_title}")

            if actual_title == expected_title:
                if expected_result =="Pass":
                    logger.info("Login Succesfull as expected")
                    login.logout()
                    test_statuses.append("Pass")
                else:
                    logger.warning("Unexpected login success")
                    capture_screenshot(self.driver,f"Unexpectedpass_row{r}",__file__)
                    login.logout()
                    test_statuses.append("Fail")
            else:
                if expected_result == "Fail":
                    logger.info("Login Failed as Expected")
                    test_statuses.append("Pass")
                else:
                    logger.warning("Unexpected login Failure")
                    capture_screenshot(self.driver,f"UnexpectedFail_Row{r}",__file__)
                    test_statuses.append("Fail")
            logger.info(f"Test Summary : {test_statuses}")

        self.driver.quit()
        assert "Fail" not in test_statuses, "Some Login tests failedr"


