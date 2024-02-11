import time
import random
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from typing import Union, Any, List

def CustomSeleniumDecorator(func):
    def wrapper(self, *args, **kwargs):
        try:
            if self._error:
                return False
            res = func(self, *args, **kwargs)
            self._reload_count = 0
            return res
        except Exception as e:
            print(e)
            if "about:neterror" in str(e) and self._reload_count < self._max_reload_count:
                self._reload_count += 1
                self.waitFor(5)
                self.goRefresh()
                return True
            self._error = True
            return False

    return wrapper

class BasePage():
    def __init__(self, driver: webdriver.Chrome) -> None:
        
        logger = logging.getLogger('selenium')
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler = logging.FileHandler('debug.log')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        self.driver = driver
        self._error = False
        self._reload_count = 0
        self._max_reload_count = 10
        self.driver.implicitly_wait(10)
        self._max_time_wait_element = 10
        

    @CustomSeleniumDecorator
    def findElement(self, by :By, value :str) -> Union[WebElement, bool]:
        try:
            element = WebDriverWait(self.driver, self._max_time_wait_element).until(
                ec.presence_of_element_located((by, value))
            )
            return element
        except Exception:
            print(f"Element:{value} not found")
            return False
    
    @CustomSeleniumDecorator
    def findElementAll(self, by :By, value :str) -> Union[WebElement, List[WebElement], bool]:
        try:
            elements = WebDriverWait(self.driver, self._max_time_wait_element).until(
                ec.presence_of_all_elements_located((by, value))
            )
            return elements
        except Exception:
            print(f"Elements:{value} not found")
            return False

    #----------------------------------------WORK WITH WINDOWS----------------------------------------
    
    @CustomSeleniumDecorator
    def getWindowsHandles(self) -> List[str]:
        return self.driver.window_handles

    @CustomSeleniumDecorator
    def switchToNewWindow(self) -> bool:
        windows = self.getWindowsHandles()
        self.switchWindow(windows[-1])
        return True
    
    @CustomSeleniumDecorator
    def newWindow(self, url = "about:blank") -> bool:
        self.executeScript(f'window.open("{url}","_blank");')
        return True

    @CustomSeleniumDecorator
    def switchWindow(self, window_id :str) -> bool:
        self.driver.switch_to.window(window_id)
        return True

    @CustomSeleniumDecorator
    def closeWindow(self) -> bool:
        self.driver.close()
        return True

    @CustomSeleniumDecorator
    def closeBrowser(self) -> bool:
        self.driver.quit()
        return True

    #----------------------------------------WORK WITH PAGE----------------------------------------

    @CustomSeleniumDecorator
    def goToUrl(self, url :str) -> bool:
        self.driver.get(url)
        return True

    @CustomSeleniumDecorator
    def getCurrentUrl(self) -> str:
        return self.driver.current_url

    @CustomSeleniumDecorator
    def goForward(self) -> bool:
        self.driver.forward()
        return True

    @CustomSeleniumDecorator
    def goBack(self) -> bool:
        self.driver.back()
        return True

    @CustomSeleniumDecorator
    def goRefresh(self) -> bool:
        self.driver.refresh()
        return True

    @CustomSeleniumDecorator
    def getPageSource(self) -> str:
        return self.driver.page_source

    @CustomSeleniumDecorator
    def switchFrame(self, by :By, value :str) -> bool:
        self.driver.switch_to.frame(self.findElement(by, value))
        return True

    @CustomSeleniumDecorator
    def switchDefaultContent(self) -> bool:
        self.driver.switch_to.default_content()
        return True

    @CustomSeleniumDecorator
    def executeScript(self, script :str) -> Any:
        return self.driver.execute_script(script)
    
    @CustomSeleniumDecorator
    def waitFor(self, value :float) -> None:
        time.sleep(value)

    @CustomSeleniumDecorator
    def waitHumanizer(self) -> None:
        time.sleep(random.uniform(1, 2.5))
    
    @CustomSeleniumDecorator
    def getTitle(self) -> str:
        return self.driver.title
    
    #----------------------------------------WORK WITH ELEMENTS----------------------------------------

    @CustomSeleniumDecorator
    def clickTo(self, by :By, value :str) -> bool:
        try:
            self.findElement(by, value).click()
            self.waitHumanizer()
            return True
        except Exception:
            return False
    
    @CustomSeleniumDecorator
    def scrollTo(self, x :int = 0, y :int = 150) -> Any:
        return self.executeScript("window.scrollTo({left: window.scrollX + %i, top: window.scrollY + %i, behavior: 'smooth'})" % (x, y))

    @CustomSeleniumDecorator
    def scrollToElem(self, by :By, value :str) -> Any:
        try:
            self.findElement(by, value).location_once_scrolled_into_view
            time.sleep(1.5)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.PAGE_DOWN).perform()
            return True
        except Exception:
            return False
        
    @CustomSeleniumDecorator
    def sendKeysToElement(
        self,
        by :By,
        value :str,
        text :str,
        min_wait :float = 0.05,
        max_wait :float = 0.2,
        full :bool = False
    ) -> bool:
        if elem:=self.findElement(by, value):
            if full:
                elem.send_keys(text)
            else:
                for char in text:
                    elem.send_keys(char)
                    self.waitFor(random.uniform(min_wait, max_wait))
            return True
        else:
            return False

    @CustomSeleniumDecorator
    def clearElement(self, by :By, value :str) -> bool:
        self.findElement(by, value).clear()
        return True

    @CustomSeleniumDecorator
    def waitForElement(self, by :By, value :str, timeout :float = 45) -> Union[WebElement, bool]:
        try:
            return WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located((by, value))
            )
        except Exception:
            return False
    
    @CustomSeleniumDecorator
    def waitForUrlChanges(self, current_url :str, timeout :float = 90) -> bool:
        return WebDriverWait(self.driver, timeout).until(
            ec.url_changes(current_url)
        )

    #----------------------------------------SKRIN----------------------------------------
    def screenshot(self, file_name :str) -> bool:
        return self.driver.get_screenshot_as_file(file_name)
 