import pytest
from selenium import webdriver
from utilities.driver_factory import DriverFactory
from utilities.api_client import APIClient
from utilities.logger import setup_logger
import config

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                    help="Browser for UI tests: chrome/firefox")
    parser.addoption("--env", action="store", default="staging",
                    help="Test environment: dev/staging/prod")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def logger():
    return setup_logger()

@pytest.fixture(scope="function")
def driver(request, env, logger):
    browser = request.config.getoption("--browser")
    driver = DriverFactory.get_driver(browser)
    driver.maximize_window()
    base_url = getattr(config, f"{env.upper()}_URL")
    driver.get(base_url)
    
    yield driver
    
    driver.quit()

@pytest.fixture(scope="session")
def api_client(env):
    base_url = getattr(config, f"{env.upper()}_API_URL")
    return APIClient(base_url)
