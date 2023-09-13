from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    firstName = browser.find_element(By.NAME, 'firstname')
    lastName = browser.find_element(By.NAME, 'lastname')
    eMail = browser.find_element(By.NAME, 'email')
    uploadBtn=browser.find_element(By.ID,'file')
    submitBtn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

    firstName.send_keys('Eziz')
    lastName.send_keys('Annamyradov')
    eMail.send_keys('Eziz@mail.ru')

    currentDir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(currentDir,'Eziz.txt')

    uploadBtn.send_keys(file_path)
    submitBtn.click()
finally:
    time.sleep(15)
    browser.quit()
