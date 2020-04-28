# https://stepik.org/lesson/138920/step/10?unit=196194
from selenium import webdriver
import time

delay = 10
link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath("//input[@class=\"form-control first\" and @required]").send_keys("first")
    browser.find_element_by_xpath("//input[@class=\"form-control second\" and @required]").send_keys("second")
    browser.find_element_by_xpath("//input[@class=\"form-control third\" and @required]").send_keys("third@email.com")

    browser.find_element_by_css_selector("button.btn").click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(delay)
    browser.quit()
