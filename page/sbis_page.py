import os
import time
import re

from typing import List

from .base_page import BasePage
from .locators import *
from .user import UserSettings


class SbisPage(BasePage):
    def go_to_contact(self) -> None:
        self.clickTo(*SbisLocators.CONTACTS_LOCATOR)
    
    def go_to_tenzor_page(self) -> None:
        self.clickTo(*SbisLocators.LOGO_TENSOR_LOCATOR)
        self.switchToNewWindow()
    
    def chek_my_region(self) -> bool:
        if (
            (_region :=self.findElement(*SbisLocators.REGION_LOCATOR)) and
            (_contact_list :=self.findElementAll(*SbisLocators.CONTACTS_LIST_LOCATOR))
        ):  
            print(f"\033[1;32mYou region {_region.text}, count contact: {len(_contact_list)}\033[0m")
            return True
        else:
            print("\033[1;31;40mError find region\033[0m")
            return False
        
    def region_compliance(self, region:str, region_url:str, city_list:List[str]) -> bool:
        if (
            (_region :=self.findElement(*SbisLocators.REGION_LOCATOR)) and
            (_city_list :=[city.text for city in self.findElementAll(*SbisLocators.CHOICE_REGION_CITYS_LOCATOR)]) and
            (_region_url :=self.getCurrentUrl()) and
            (_title :=self.getTitle())
        ):  
            if (
                region in _region.text and
                _region_url.split('contacts/')[1].split('?')[0] == region_url and
                region in _title and
                all(city in _city_list for city in city_list)
            ):  
                print("\033[1;32mRegion match\033[0m")
                return True
            else:
                print("\033[1;31;40mRegion don`t match\033[0m")
                return False
        else:
            print("\033[1;31;40mError find region\033[0m")
            return False
    
    def change_my_region(self) -> None:
        self.clickTo(*SbisLocators.REGION_LOCATOR)
        self.clickTo(*SbisLocators.CHOICE_REGION_LOCATOR)
    
    def go_to_download_page(self) -> None:
        self.waitHumanizer()
        self.scrollToElem(*SbisLocators.DOWNLOAD_LOCATOR)
        self.waitHumanizer()
        self.clickTo(*SbisLocators.DOWNLOAD_LOCATOR)
    
    def download_plugin_web(self) -> None:
        self.waitHumanizer()
        self.clickTo(*SbisLocators.BUTTON_PLUGIN_LOCATOR)
        self.waitHumanizer()        
        self.clickTo(*SbisLocators.BUTTON_DOWNLOAD_LOCATOR)

    def wait_file_download(self) -> bool:
        url_file = self.findElement(*SbisLocators.BUTTON_DOWNLOAD_LOCATOR).get_attribute('href')
        file_path = os.path.join(os.getcwd(), os.path.basename(url_file))
        start_time = time.time()
        while not os.path.exists(file_path):
            if time.time() - start_time > UserSettings.TIMEOUT_DOWNLOAD_FILE_SEC:
                print("\033[1;31;40mTimeout download file\033[0m")
                return False
            time.sleep(1)
        print("\033[1;32mFile is uploaded\033[0m")
        return True

    def chek_size_file(self) -> bool:
        download_button = self.findElement(*SbisLocators.BUTTON_DOWNLOAD_LOCATOR)
        url_file = download_button.get_attribute('href')
        size_file = float(re.findall(r"(\d+\.\d+)\sМБ", download_button.text)[0])
        file_path = os.path.join(os.getcwd(), os.path.basename(url_file))
        if os.path.exists(file_path):
            file_size_mb = round(os.path.getsize(file_path) / (1024 * 1024), 2)
            if size_file == file_size_mb:
                print("\033[1;32mFile is correct\033[0m")
                return True
            else:
                print("\033[1;31;40mThe file size is incorrect\033[0m")
                return False
        else:
            print("\033[1;31;40mFile was not found\033[0m")
            return False
        
    def open(self, link: str) -> None:
       self.goToUrl(link)
       self.waitHumanizer()