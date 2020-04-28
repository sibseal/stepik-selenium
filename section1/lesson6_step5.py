# https://stepik.org/lesson/138920/step/5?unit=196194
from selenium import webdriver
import time
import math

delay = 10
link = "http://suninjuly.github.io/find_link_text"
code = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:

    browser = webdriver.Chrome()
    browser.get(link)
    input = browser.find_element_by_partial_link_text(code)
    input.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(delay)
    browser.quit()
