import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from  my_date import *

options = Options()
options.add_argument(f"user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0")
driver = webdriver.Chrome(
    executable_path="/home/object/PycharmProjects/VK/chromedriver",
    options=options
    )
url = "https://vk.com"

try:

    #IN_VK
    driver.get(url=url)
    driver.get_screenshot_as_file("screen.png")
    driver.refresh()
    time.sleep(random.randint(1, 3))

    #LOGIN
    email = driver.find_element(By.ID, "index_email")
    email.clear()
    email.send_keys(f"{login}")
    # email.send_keys(Keys.ENTER)
    alien_button = driver.find_element(By.CLASS_NAME, "VkIdCheckbox")
    alien_button.click()
    time.sleep(random.randint(1, 3))
    button = driver.find_element(By.ID, "index_rcolumn").find_element(By.CLASS_NAME, "FlatButton__in")
    button.click()
    time.sleep(random.randint(1, 3))

    #PASS
    password = driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys(f"{password_}")
    # password.send_keys(Keys.ENTER)
    i_see_you = driver.find_element(By.CLASS_NAME, "vkc__Password__ViewIcon")
    i_see_you.click()
    time.sleep(random.randint(1, 3))
    button_pass = driver.find_element(By.CLASS_NAME, "vkc__EnterPasswordNoUserInfo__buttonWrap")
    button_pass.click()
    time.sleep(random.randint(1, 3))

    #PIN
    pin = driver.find_element(By.NAME, "otp")
    pin.send_keys(f"{pin_}")
    time.sleep(random.randint(1, 3))
    try:
        save_button = driver.find_element(By.CLASS_NAME, "vkc__Checkbox__wrapper")
        save_button.click()
        time.sleep(random.randint(1, 3))
    except:
        time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
