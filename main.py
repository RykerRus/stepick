from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

value = int(browser.find_element_by_css_selector('span#num1').text)
value2 = int(browser.find_element_by_css_selector('span#num2').text)
s = browser.find_element_by_css_selector('select.custom-select')
s.click()
s.find_element_by_css_selector(f'option[value="{value + value2}"]').click()


button = browser.find_element_by_css_selector("button[type=submit]")
button.click()

time.sleep(1)
