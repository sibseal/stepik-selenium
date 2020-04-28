# https://stepik.org/lesson/228249/step/8?unit=200781
from selenium import webdriver
import time
import os

delay = 10
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath("//input[@name=\"firstname\" and @required]").send_keys("first")
    browser.find_element_by_xpath("//input[@name=\"lastname\" and @required]").send_keys("last")
    browser.find_element_by_xpath("//input[@name=\"email\" and @required]").send_keys("email@example.com")

    file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'upload.txt')
    file.send_keys(file_path)

    submit = browser.find_element_by_css_selector("[type=\"submit\"]")
    submit.click()
finally:
    time.sleep(delay)
    browser.quit()
