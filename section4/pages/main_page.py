from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def go_to_login_page_new(self):
        login_link = self.browser.find_element(By.ID, "registration_link")
        login_link.click

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

    def should_be_login_link_new(self):
        assert self.is_element_present(By.ID, "registration_link"), "Login link is not presented"
