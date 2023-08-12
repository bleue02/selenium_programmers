import platform
import time
from tqdm import tqdm
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from func import get_login_option, login_info, login_info_xpath, login_info_google_xpath, login_google_info
import subprocess
from selenium.webdriver.chrome.options import Options
from option_box import check_box_level
from selenium.webdriver.chrome.service import Service

def get_chrome_executable():
    system = platform.system()
    if system == "Windows":
        return "C:/Program Files/Google/Chrome/Application/chrome.exe"
    elif system == "Darwin":  # macOS
        return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    elif system == "Linux":
        return "/usr/bin/google-chrome"  # 또는 "/usr/bin/chromium-browser"
    else:
        raise OSError("Unsupported operating system")

def auto_selenium_login():
    def progress_bar():
        progress_bars = tqdm(total=100, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}')
        progress_bars.set_description(f'{get_login_option(user_select).split()[-2]} 진행중...')
        progress_bars.update(10)
        driver.set_window_size(400, 700)

        progress_bars.update(50)
        progress_bars.set_description(f'{get_login_option(user_select).split()[-2]} 완료됨.')
        progress_bars.update(40)
        progress_bars.close()

    print(f'{get_login_option(1)}\n'
          f'{get_login_option(2)}\n'
          f'{get_login_option(3)}\n'
          f'{get_login_option(4)}\n'
          f'{get_login_option(5)}\n'
          f'{get_login_option(6)}\n')

    user_select = int(input('Please enter the login option: '))

    if user_select in [1, 2, 4, 5, 6]:
        user_id = input(f'{get_login_option(user_select).split()[-2]} ID: ')
        user_password = input(f'{get_login_option(user_select).split()[-2]} PASSWORD: ')
        clear()

        login_url = login_info(str(user_select))

        if login_url:
            subprocess.Popen([get_chrome_executable(), "--remote-debugging-port=9222", "--user-data-dir=C:\chromeCookie"])

            option = Options()
            option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
            progress_bar()
            driver.get(login_url)
            driver.fullscreen_window()

        while True:
            xpath = login_info_xpath(user_select)
            if xpath:
                wait = WebDriverWait(driver, 10)
                id_box = wait.until(EC.element_to_be_clickable((By.XPATH, xpath[f'{user_select}_Id_Box'])))
                time.sleep(0.01)
                password_box = wait.until(EC.element_to_be_clickable((By.XPATH, xpath[f'{user_select}_Pswd_Box'])))
                time.sleep(0.01)
                login_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath[f'{user_select}_Submit_Box'])))

            else:
                print('Invalid login options.')
                driver.quit()
                break

            act = ActionChains(driver)
            act.send_keys_to_element(id_box, user_id).send_keys_to_element(password_box, user_password).click(login_button).perform()
            time.sleep(3)
            driver.find_element(By.LINK_TEXT, '코딩테스트 연습').click()
            driver.fullscreen_window()
            time.sleep(3)
            check_box_level(driver, selected_level)

    elif user_select == 3: # google Login
        google_ID = input(f'{get_login_option(user_select).split()[-2]} ID: ')
        google_PSWD = input(f'{get_login_option(user_select).split()[-2]} PSWD: ')

        specific_url = login_google_info().get('3')

        subprocess.Popen([get_chrome_executable(), "--remote-debugging-port=9222", "--user-data-dir=C:\chromeCookie"])

        option = Options()
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        drivers = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        drivers.set_window_size(414, 800)
        drivers.get(specific_url)
        drivers.find_element(By.LINK_TEXT, '코딩테스트 연습').click()

        google_Id_Box_xpath = login_info_google_xpath()['google_Id_Box'] # ID Box
        google_Pswd_Box_xpath = login_info_google_xpath()['google_Pswd_Box'] # Pswd Box
        google_Id_Submit_Box = login_info_google_xpath()['google_Id_Submit_Box'] # ID Submit Box
        google_Pswd_submit_box = login_info_google_xpath()['google_Pswd_submit_box'] # ID Submit Box

        wait_google = WebDriverWait(drivers, 5)

        time.sleep(3)
        google_Id_Box = wait_google.until(EC.element_to_be_clickable((By.XPATH, google_Id_Box_xpath))) # ID Xpath
        google_Id_Submit_Box = wait_google.until(EC.element_to_be_clickable((By.XPATH, google_Id_Submit_Box))) # ID Submit Xpath

        act_google = ActionChains(drivers) # Act Func

        act_google.send_keys_to_element(google_Id_Box, google_ID).click(google_Id_Submit_Box).perform() # ID Login

        act_google.reset_actions() # Re-User Actions Func.

        time.sleep(3)
        google_Pswd_Box = wait_google.until(EC.element_to_be_clickable((By.XPATH, google_Pswd_Box_xpath))) # PSWD Xpath
        google_Pswd_Submit_Box = wait_google.until(EC.element_to_be_clickable((By.XPATH, google_Pswd_submit_box))) # PSWd Submit Xpath

        time.sleep(3)
        act_google.send_keys_to_element(google_Pswd_Box, google_PSWD).click(google_Pswd_Submit_Box).perform() # Pswd Login

        drivers.find_element(By.LINK_TEXT, '코딩테스트 연습').click()

        time.sleep(3)
        check_box_level(drivers, selected_level)

    return driver


if __name__ == "__main__":
    from programmers_Info import clear, select_lang, select_level
    clear()
    selected_language = select_lang()
    clear()
    selected_level = select_level()
    clear()
    driver = auto_selenium_login()