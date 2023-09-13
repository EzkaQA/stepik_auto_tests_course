from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    browser.get('http://suninjuly.github.io/cats.html')

    browser.find_element(By.ID, "button")
finally:
    time.sleep(5)
    browser.quit()
    


