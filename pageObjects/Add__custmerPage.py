import time
from selenium.webdriver.support.ui import  Select

class AddCustomer:
    link_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menuitems_xpath = "//a[@href='/Admin/Customer/List']"
    link_addnew_xpath = "//a[@href='/Admin/Customer/Create']"
    input_email_xpath = "//input[@id='Email']"
    input_pass_xpath ="//input[@id='Password']"
    input_firstname_xpath = "//input[@id='FirstName']"
    input_lastname_xpath = "//input[@id='LastName']"
    radio_male_xpath ="//input[@id='Gender_Male']"
    radio_female_xpath ="//input[@id='Gender_Female']"
    input_comname_xpath ="//input[@id='Company']"
    checkbox_tax_xpath ="//input[@id='IsTaxExempt']"
    search_newsletter_xpath = "//span[@aria-expanded='true']//input[@type='search']"
    news_nopcommerce = "//span[@class='selection']//span[@role='combobox']//li[@title='nopCommerce admin demo store']"
    customer_role_input ="//span[@aria-expanded='true']//input[@role='searchbox']"
    customerrole_li_xpath ="//li[@title='Registered']"
    checked_active_xpath='//input[@data-val-required="The Active field is required."]'
    checked_password_xpath = '//input[@data-val-required="The Customer must change password field is required."]'
    text_area_comment_xpath ='//textarea[@class="form-control"]'
    button_save_xpath ='//button[@name="save"]'

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.link_customer_menu_xpath).click()

    def cliclonCustomerMenuitems(self):
        self.driver.find_element_by_xpath(self.link_customer_menuitems_xpath).click()

    def clickOn_Addnew(self):
        self.driver.find_element_by_xpath(self.link_addnew_xpath).click()

