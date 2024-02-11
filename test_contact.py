from page.sbis_page import SbisPage
from page.tensor_page import TensorPage
from page.user import UserSettings

def test_first_scenario(driver) -> None:
    link = "https://sbis.ru/"
    sbis_page = SbisPage(driver)  
    sbis_page.open(link)           
    sbis_page.go_to_contact()
    sbis_page.go_to_tenzor_page()
    tensor_page = TensorPage(driver)
    assert tensor_page.check_power_people() is True
    assert tensor_page.go_to_about() is True
    assert tensor_page.check_height_and_width_photo() is True

def test_second_scenario(driver) -> None:
    link = "https://sbis.ru/"
    sbis_page = SbisPage(driver)  
    sbis_page.open(link)
    sbis_page.go_to_contact()
    assert sbis_page.chek_my_region() is True
    sbis_page.change_my_region()
    assert sbis_page.region_compliance(
        UserSettings.CHOICE_REGION,
        UserSettings.CHOISE_REGION_URL,
        UserSettings.СHOISE_LIST_CITY
    ) is True

def test_third_scenario(driver) -> None:
    link = "https://sbis.ru/"
    sbis_page = SbisPage(driver)  
    sbis_page.open(link)
    sbis_page.go_to_download_page()
    sbis_page.download_plugin_web()
    assert sbis_page.wait_file_download() is True
    assert sbis_page.chek_size_file() is True
    
    