from selenium import webdriver
import time

delay = 10


def submit_answer(result):
    try:
        url = "https://stepik.org"
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(delay)

        # login = browser.find_element_by_css_selector("a.navbar__auth.navbar__auth_type_login.st-link.st-link_style_button.navbar__auth_only_desktop.ember-link.ember-view")
        login = browser.find_element_by_xpath("//a[text()=\"Войти\"]")
        login.click()
        email = browser.find_element_by_id("id_login_email")
        email.send_keys("a.adushkin@inbox.ru")
        password = browser.find_element_by_id("id_login_password")
        password.send_keys("F}Xj2ixxoEgX")
        enter = browser.find_element_by_css_selector(".sign-form__btn.button_with-loader")
        enter.click()
        time.sleep(delay)

        url = "https://stepik.org/lesson/184253/step/4"
        browser.get(url)
        time.sleep(delay)

        textarea = browser.find_element_by_css_selector("textarea[placeholder=\"Напишите ваш ответ здесь...\"]")
        textarea.send_keys(result)
        submit = browser.find_element_by_css_selector("button.submit-submission")
        submit.click()

        time.sleep(delay)
    finally:
        browser.quit()
