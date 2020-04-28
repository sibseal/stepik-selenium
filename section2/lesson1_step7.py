# https://stepik.org/lesson/165493/step/7?unit=140087
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


delay = 10
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id("treasure")
    value = treasure.get_attribute("valuex")
    result = calc(value)

    browser.find_element_by_id("answer").send_keys(result)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("[type=\"submit\"]").click()


finally:
    time.sleep(delay)
    browser.quit()
