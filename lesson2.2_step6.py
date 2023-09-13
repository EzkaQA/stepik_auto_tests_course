from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    xDefinition = browser.find_element(By.ID, 'input_value').text
    inputField = browser.find_element(By.ID, 'answer')
    y = calc(xDefinition)
    inputField.send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkBox = browser.find_element(By.ID, 'robotCheckbox').click()

    robotRuleRadioBtn = browser.find_element(By.ID, 'robotsRule').click()

    button.click()
finally:
    time.sleep(15)
    browser.quit()
