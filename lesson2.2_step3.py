from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
browser = webdriver.Chrome()

try:
    browser.get('https://suninjuly.github.io/selects1.html')
    first_num = int(browser.find_element(By.ID, 'num1').text)
    second_num = int(browser.find_element(By.ID, 'num2').text)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    #summ =str(first_num + second_num)
    select.select_by_value(str(first_num+second_num))
    submitBtn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submitBtn.click()
finally:
    time.sleep(15)
    browser.quit()
    browser.switch_to.alert


    
