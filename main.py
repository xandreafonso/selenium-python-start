import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

browser.get('https://site.com')

element = browser.find_element(By.XPATH, '//*[@id="inf_field_Email"]')
element.send_keys('afonsoaaf@gmail.com')

time.sleep(10) # segundos

def wait(browser, xpath):
  try:
    return WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
  finally:
    browser.quit()