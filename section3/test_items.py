import time


def test_check_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(link)
    button_add_to_basket = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    time.sleep(30)
    assert button_add_to_basket is not None
