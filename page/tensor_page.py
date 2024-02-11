from .base_page import BasePage
from .locators import *

class TensorPage(BasePage):
    def check_power_people(self) -> bool:
        if self.findElement(*TensorLocators.TITLE_POWER_PEOPLE_LOCATOR):
            print("\033[1;32mLocator 'Сила в людях' found\033[0m")
            return True
        else:
            print("\033[1;31;40mLocator 'Сила в людях' not found\033[0m")
            return False
    
    def go_to_about(self) -> bool:
        self.waitHumanizer()
        self.scrollToElem(*TensorLocators.ABOUT_LOCATOR)
        self.waitHumanizer()
        self.clickTo(*TensorLocators.ABOUT_LOCATOR)
        if self.getCurrentUrl() == 'https://tensor.ru/about':
            print("\033[1;32mUrl /about confirm\033[0m")
            return True
        else:
            print("\033[1;31;40mUrl /about error\033[0m")
            return False
    
    def check_height_and_width_photo(self) -> bool:
        self.waitHumanizer()
        self.scrollToElem(*TensorLocators.PHOTOS_LOCATOR)
        self.waitHumanizer()
        photos = self.findElementAll(*TensorLocators.PHOTOS_LOCATOR)
        if photos:
            first_photo = photos[0]
            width = first_photo.get_attribute('width')
            height = first_photo.get_attribute('height')

            for photo in photos[1:]:
                if photo.get_attribute('width') != width or photo.get_attribute('height') != height:
                    print("\033[1;31;40mThe photos have different sizes\033[0m")
                    return False
            print("\033[1;32mThe photos are of the same size\033[0m")
            return True
        else:
            print("\033[1;31;40mNone photos\033[0m")
            return False
           
    def open(self, link:str) -> None:
       self.goToUrl(link)