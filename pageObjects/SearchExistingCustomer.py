

from  selenium.webdriver.common.by import By



class search_existingcustomer:
    id_email_text = "SearchEmail"
    id_firstname_text = "SearchFirstName"
    id_lastname_text = "SearchLastName"
    id_search_btn = "search-customers"
    id_table_grid = '//table[@id="customers-grid"]'
    xpath_table_rows = '//table[@id="customers-grid"]//tbody/tr'
    xpath_table_columns = '//table[@id="customers-grid"]//tbody/tr/td'


    def __init__(self, driver):
        self.driver = driver

    def setByemail(self,value):
        self.driver.find_element(By.ID,self.id_email_text).clear()
        self.driver.find_element(By.ID,self.id_email_text).send_keys(value)

    def setbyFistname(self,value):
        self.driver.find_element(By.ID,self.id_firstname_text).clear()
        self.driver.find_element(By.ID, self.id_firstname_text).send_keys(value)

    def setBylastname(self,value):
        self.driver.find_element(By.ID,self.id_lastname_text).clear()

        self.driver.find_element(By.ID,self.id_lastname_text).send_keys(value)

    def clickSearch(self):
        self.driver.find_element(By.ID,self.id_search_btn).click()

    def getNofRows(self):
        return  len(self.driver.find_elements(By.XPATH,self.xpath_table_rows))

    def getNoofColumns(self):
        return  len(self.driver.find_elements(By.XPATH, self.xpath_table_columns))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getNofRows() + 1):
            table = self.driver.find_element(By.XPATH,self.id_table_grid)
            emailid = table.find_element(By.XPATH,'//table[@id="customers-grid"]//tbody/tr/td[2]').text
            if emailid == email:
                flag = True
                break

        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.id_table_grid)
            name = table.find_element(By.XPATH, '//table[@id="customers-grid"]//tbody/tr/td[3]').text
            if name == Name:
                flag = True
                break

        return flag

