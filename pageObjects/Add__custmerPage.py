import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddCustomer:
    link_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menuitems_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_addnew_xpath = "//a[@href='/Admin/Customer/Create']"
    input_email_xpath = "//input[@id='Email']"
    input_pass_xpath = "//input[@id='Password']"
    input_firstname_xpath = "//input[@id='FirstName']"
    input_lastname_xpath = "//input[@id='LastName']"
    radio_male_xpath = "//input[@id='Gender_Male']"
    radio_female_xpath = "//input[@id='Gender_Female']"
    input_comname_xpath = "//input[@id='Company']"
    checkbox_tax_xpath = "//input[@id='IsTaxExempt']"
    search_newsletter_xpath = "//input[@class='select2-search__field']"
    news_nopcommerce = "//span[@class='selection']//span[@role='combobox']//li[@title='nopCommerce admin demo store']"
    customer_role_input = "//span[@aria-expanded='true']//input[@role='searchbox']"
    customerrole_li_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-c5mh-3']"
    select_vendors_id = '//select[@id="VendorId"]'
    checked_active_xpath = "//input[@id='Active']"

    checked_password_xpath = '//input[@data-val-required="The Customer must change password field is required."]'
    text_area_comment_xpath = '//textarea[@class="form-control"]'
    button_save_xpath = '//button[@name="save"]'

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        xpath = self.link_customer_menu_xpath

        for attempt in range(2):
            try:
                # Wait for overlays/loaders to disappear, if any
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, ".overlay, .loading, .spinner"))
                )

                # Wait until clickable
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )

                # Scroll into view before clicking
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

                # Try clicking
                element.click()
                return  # Success, exit method

            except Exception as e:
                print(f"Attempt {attempt + 1} to click menu failed. Retrying... Error: {e}")
                time.sleep(1)

        # Final fallback - JavaScript click
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            self.driver.execute_script("arguments[0].click();", element)
            print("JS click worked as fallback.")
        except Exception as final_e:
            print(f"JS click also failed. Reason: {final_e}")

    def clickOnCustomerMenuitems(self):
        WebDriverWait(self.driver,timeout=100).until(
            EC.element_to_be_clickable((By.XPATH,self.link_customer_menuitems_xpath))
        ).click()
        WebDriverWait(self.driver, timeout=100).until(
            EC.element_to_be_clickable((By.XPATH, self.link_customer_menuitems_xpath))
        ).click()
    def clickonCustomerMenuitems_dropdown(self):
        WebDriverWait(self.driver,timeout=10).until(
            EC.element_to_be_clickable((By.XPATH,self.link_customer_dropdown_menuitems_xpath))
        ).click()

    def clickOn_Addnew(self):
        time.sleep(10)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_addnew_xpath))
        ).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.input_pass_xpath).send_keys(password)

    def setfirstname(self, name):
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).send_keys(name)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).send_keys(lastname)

    def setgender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.radio_male_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.radio_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.radio_male_xpath).click()

    def setCompanyName(self, CmpName):
        self.driver.find_element(By.XPATH, self.input_comname_xpath).send_keys(CmpName)

    def taxextempt(self):
        self.driver.find_element(By.XPATH, self.checkbox_tax_xpath).click()

    def newsletter(self, options):
        self.driver.find_element(By.XPATH, self.search_newsletter_xpath).click()
        time.sleep(1)
        if options == "nopCommerce admin demo store":
            self.driver.find_element(By.XPATH, self.news_nopcommerce).click()
        else:
            self.driver.find_element(By.XPATH, self.news_nopcommerce).click()

    def setCumstomerrole(self):
        self.driver.find_element(By.XPATH, self.customer_role_input).click()

        # if role == "Registered":
        #
        # else:
        # #     self.role_item = self.driver.find_element(By.XPATH, self.customerrole_li_xpath)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.role_item)
        # time.sleep(1)  # Optional: add short wait for scroll to complete
        #
        # self.driver.execute_script("arguments[0].click();",self.role_item)

    def selectRegistrer(self):
        self.driver.find_element(By.XPATH, self.customerrole_li_xpath)

    def setMangerofvendor(self, value):
        vendor_dropdown = Select(self.driver.find_element(By.XPATH, self.select_vendors_id))
        vendor_dropdown.select_by_visible_text(value)

    def active_checkbox(self):
        self.driver.find_element(By.XPATH, self.checked_active_xpath).click()

    def customerchangedpassword(self):
        self.driver.find_element(By.XPATH, self.checked_password_xpath).click()

    def adminComment(self, comment):
        self.driver.find_element(By.XPATH, self.text_area_comment_xpath).send_keys(comment)

    def saveCustomerdetails(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()
