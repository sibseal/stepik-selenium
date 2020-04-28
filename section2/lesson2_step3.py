# https://stepik.org/lesson/228249/step/3?unit=200781
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


delay = 10
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    n1 = int(browser.find_element_by_id("num1").text)
    print(n1)
    n2 = int(browser.find_element_by_id("num2").text)
    print(n2)
    result = n1 + n2
    print(result)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(result))

    submit = browser.find_element_by_css_selector("[type=\"submit\"]")
    submit.click()
finally:
    time.sleep(delay)
    browser.quit()
