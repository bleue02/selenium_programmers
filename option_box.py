import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from programmers_Info import coding_Language_xpath, coding_Level_xpath, coding_Language_xpath_numbers
from programmers_Info import select_level, select_lang


def check_box_level(driver, user_select_level):
    option = Options()
    option.add_experimental_option('detach', True)
    wait = WebDriverWait(driver, 30)

    # level DropBox
    levels = coding_Level_xpath()
    level = f'Level.{user_select_level}'
    level_xpath = levels.get(level)

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='title'])[2]"))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, level_xpath))).click()

# -----------------------------------------------------------------------------

    wait = WebDriverWait(driver, 30)
    from programmers_Info import user_select_languages
    # user_select_language,_ = user_select_languages  # Lang DropBox
    langs = coding_Language_xpath_numbers()
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='title'])[3]"))).click()
    lang_xpath = langs[user_select_languages]
    wait.until(EC.element_to_be_clickable((By.XPATH, lang_xpath))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='title'])[3]"))).click()