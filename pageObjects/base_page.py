import os
import logging
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from  selenium.common.exceptions import  NoSuchElementException, TimeoutException
from  selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)
        if not os.path.exists("Screenshots"):
            os.mkdir("Screenshots")


    def wait_for_element(self, by_locator, condition = EC.visibility_of_element_located):
        try:
            return WebDriverWait(self.driver, self.timeout).until(condition(by_locator))
        except TimeoutException:
            self.logger.error(f"Timeout while waiting for : {by_locator}")
            self.take_screenshots(f"error_{by_locator[1]}")


    def do_send_keys(self, bylocator, value):
        try:
            element  =  self.wait_for_element(bylocator)
            element.clear()
            self.highlight_element(element)
            element.send_keys(value)
        except Exception as e:
            self.logger.error(f"Error sending keys to element {bylocator}")
            self.take_screenshots(f"send_keys_error_{bylocator[1]}")
            raise

    def do_click(self, by_locator):
        try:
            element = self.wait_for_element(by_locator)
            self.highlight_element(element)
            element.click()
        except Exception as e:
            self.logger.error(f"Error clicking on element {by_locator} : {e}")
            self.take_screenshots(f"click_error{by_locator[1]}")
            raise

    def get_text(self, by_locator):
        try:
            element = self.wait_for_element(by_locator)
            return element.text
        except Exception as e:
            self.logger.error(f"Error getting text from {by_locator}: {e}")
            self.take_screenshots(f"take_error_{by_locator[1]}")
            raise








    def take_screenshots(self, name):
        timestamp =  time.strftime("%Y%m%d-%H%M%S")
        filename = f"Screenshots/{name}_{timestamp}.png"

        try:
            self.driver.save_screenshots(filename)
            self.logger.info(f"Screenshot saved : {filename}")
        except Exception as e:
            self.logger.error(f"Failed to save screenshots : {e}")


    def highlight_element(self, element):
        try:
            self.driver.execute_script("aruguments[0].style.border='3px solid red ")
        except Exception as e:
            self.logger.error(f"Failed to highlight element : {e}")
