from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/alert_accept.html')
    firstPageBtn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text
    inputX = calc(x)

    inpurField = browser.find_element(By.ID, 'answer').send_keys(inputX)

    submitBtn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(15)
    browser.quit()



