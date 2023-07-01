from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

URL = 'https://ticketmaster.sg/activity/detail/23_charlieputh'

def clickButton(driver, xpath):
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    driver.execute_script("arguments[0].scrollIntoView();", button)
    driver.execute_script("arguments[0].click();", button)


def main():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get(URL)
    driver.maximize_window()

    clickButton(driver, '//*[@id="main-container"]/section[2]/div/div/div[2]/a')
    clickButton(driver, '//*[@id="23_charlieputh-713b7c64"]/td[4]/a')

if __name__ == "__main__":
    main()