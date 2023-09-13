from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

linkMath = 'https://suninjuly.github.io/math.html'
try:
    browser.get(linkMath)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answerField = browser.find_element(By.ID, 'answer')
    answerField.send_keys(y)
    checkBox = browser.find_element(By.ID, 'robotCheckbox')
    checkBox.click()
    robotRuleRadioBtn = browser.find_element(By.ID, 'robotsRule')
    robotRuleRadioBtn.click()
    submitBtn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submitBtn.click()
finally:
    time.sleep(15)
    browser.quit()