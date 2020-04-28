# https://stepik.org/lesson/184253/step/6?unit=158843
from selenium import webdriver
import time
import math

delay = 10


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element_by_css_selector("[class=\"trollface btn btn-primary\"]")
    submit.click()
    handles = browser.window_handles
    browser.switch_to.window(handles[-1])

    x = browser.find_element_by_id("input_value").text
    result = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)

    submit = browser.find_element_by_css_selector("[type=\"submit\"]")
    submit.click()

    alert = browser.switch_to.alert
    submit_it = str(alert.text).split(" ")[-1]
    alert.accept()
    submit_answer(submit_it)

finally:
    time.sleep(delay)
    browser.quit()
