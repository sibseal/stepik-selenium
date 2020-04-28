# https://stepik.org/lesson/228249/step/6?unit=200781
from selenium import webdriver
import time
import math

delay = 10
link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id("input_value").text)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))

    checkbox = browser.find_element_by_id("robotCheckbox")
    radio = browser.find_element_by_id("robotsRule")
    submit = browser.find_element_by_css_selector("[type=\"submit\"]")


    browser.execute_script("window.scrollBy(0, 100);", checkbox)
    checkbox.click()
    browser.execute_script("window.scrollBy(0, 100);", radio)
    radio.click()
    browser.execute_script("window.scrollBy(0, 100);", submit)
    submit.click()
finally:
    time.sleep(delay)
    browser.quit()
