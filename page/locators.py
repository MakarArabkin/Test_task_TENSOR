from selenium.webdriver.common.by import By

from .user import UserSettings

class SbisLocators():
    CONTACTS_LOCATOR = (By.CSS_SELECTOR, ".sbisru-Header a[href='/contacts']")
    LOGO_TENSOR_LOCATOR = (By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor')
    
    REGION_LOCATOR = (By.CSS_SELECTOR, '.sbisru-Contacts .sbis_ru-Region-Chooser__text')
    CHOICE_REGION_LOCATOR = (By.CSS_SELECTOR, f'.sbis_ru-Region-Panel [title*="{UserSettings.CHOICE_REGION}"]')
    CHOICE_REGION_CITYS_LOCATOR = (By.CSS_SELECTOR, '.sbisru-Contacts-City__item-name')
    CONTACTS_LIST_LOCATOR = (By.CSS_SELECTOR, '#contacts_list .sbisru-Contacts-List__item')
    
    DOWNLOAD_LOCATOR = (By.CSS_SELECTOR, '.sbisru-Footer__cell:nth-child(3) .sbisru-Footer__list-item:nth-child(8) a')
    BUTTON_PLUGIN_LOCATOR = (By.CSS_SELECTOR, '[data-id="plugin"]')
    BUTTON_DOWNLOAD_LOCATOR = (By.CSS_SELECTOR, '[href*="sbisplugin-setup-web"]')

class TensorLocators():
    TITLE_POWER_PEOPLE_LOCATOR = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-Index__card-title')
    ABOUT_LOCATOR = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-link')
    PHOTOS_LOCATOR = (By.CSS_SELECTOR, '.tensor_ru-About__block3-image-wrapper img')