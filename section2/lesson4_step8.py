# https://stepik.org/lesson/181384/step/8?unit=156009
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


delay = 10

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # browser.implicitly_wait(6)

    is_continue = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    if is_continue:
        book = browser.find_element_by_id("book")
        print(book)
        book.click()
        x = browser.find_element_by_id("input_value").text
        answer = browser.find_element_by_id("answer")
        answer.send_keys(calc(x))
        solve = browser.find_element_by_id("solve")
        solve.click()

finally:
    time.sleep(delay)
    browser.quit()
