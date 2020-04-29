# https://stepik.org/lesson/36285/step/13?unit=162401
from selenium import webdriver
import time
import unittest

delay = 10


class TestRequired(unittest.TestCase):
    def test_version1(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element_by_xpath("//input[@class=\"form-control first\" and @required]").send_keys("first")
        browser.find_element_by_xpath("//input[@class=\"form-control second\" and @required]").send_keys("second")
        browser.find_element_by_xpath("//input[@class=\"form-control third\" and @required]").send_keys(
            "third@email.com")

        browser.find_element_by_css_selector("button.btn").click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(delay)
        browser.quit()

    def test_version2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element_by_xpath("//input[@class=\"form-control first\" and @required]").send_keys("first")
        browser.find_element_by_xpath("//input[@class=\"form-control second\" and @required]").send_keys("second")
        browser.find_element_by_xpath("//input[@class=\"form-control third\" and @required]").send_keys("third@email.com")

        browser.find_element_by_css_selector("button.btn").click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(delay)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
