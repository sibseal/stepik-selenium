# https://stepik.org/lesson/138920/step/7?unit=196194
from selenium import webdriver
import time

delay = 10
link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    print(elements)
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(delay)
    browser.quit()
