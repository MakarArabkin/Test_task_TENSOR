from transliterate import translit

class UserSettings():
    CHOICE_REGION = 'Камчатский край'
    CHOICE_REGION_NUM = 41
    СHOISE_LIST_CITY = ['Петропавловск-Камчатский']
    CHOISE_REGION_URL = f"{CHOICE_REGION_NUM}-{translit(CHOICE_REGION, 'ru', reversed=True).lower().replace(' ', '-')}" # or static exemple: 41-kamchatskij-kraj
    TIMEOUT_DOWNLOAD_FILE_SEC = 30