import pytest
import os

from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    options_driver = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.dirname(os.path.abspath(__file__)),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options_driver.add_experimental_option("prefs", prefs)    
    options_driver.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options_driver)
    yield driver
    print("\nquit browser..")
    driver.quit()