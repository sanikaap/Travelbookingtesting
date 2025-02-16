from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import EXPLICIT_WAIT

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
    
    def find_element(self, locator):
        """Find element with explicit wait"""
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )
    
    def click_element(self, locator):
        """Click element with explicit wait"""
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    def enter_text(self, locator, text):
        """Enter text into element with explicit wait"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from element with explicit wait"""
        element = self.find_element(locator)
        return element.text
