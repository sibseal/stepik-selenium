# https://stepik.org/lesson/237240/step/3?unit=209628
import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


class TestSecret:
    @pytest.mark.parametrize('link', links)
    def test_get_secret(self, browser: webdriver.Chrome, link):
        browser.get(link)
        textarea = browser.find_element_by_css_selector("textarea.textarea")
        answer = math.log(int(time.time()))
        textarea.send_keys(str(answer))
        submit = browser.find_element_by_css_selector("button.submit-submission")
        submit.click()
        result = browser.find_element_by_css_selector("pre.smart-hints__hint").text
        assert result == "Correct!", result
