import time

from pageObjects.loginPage import LoginPage
from pageObjects.Add__custmerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string

class Test__003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)) + "@gmail.com"

    def test_addCustomer(self, setup):
        self.logger.info("******** Test__003 AddCustomer ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.login_to_account(self.username, self.password)

        self.logger.info("********** Starting Add Customer Test ******************")

        self.addcust = AddCustomer(self.driver)
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")


        self.addcust.clickOn_Addnew()

        email = self.random_email()
        self.addcust.setEmail("jeeva1@gmail.com")
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
        self.driver.close()
