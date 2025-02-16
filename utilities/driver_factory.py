from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import os
from config import CHROME_OPTIONS

class DriverFactory:
    @staticmethod
    def get_driver(browser_name):
        """
        Factory method to get WebDriver instance based on browser name
        """
        if browser_name.lower() == "chrome":
            options = ChromeOptions()
            for option in CHROME_OPTIONS:
                options.add_argument(option)

            # Required for running Chrome in Replit
            options.binary_location = "/usr/bin/chromium"
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

            # Set up ChromeDriver service
            service = ChromeService()
            return webdriver.Chrome(service=service, options=options)

        elif browser_name.lower() == "firefox":
            options = FirefoxOptions()
            options.headless = True
            service = FirefoxService(GeckoDriverManager().install())
            return webdriver.Firefox(service=service, options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")