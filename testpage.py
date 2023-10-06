import logging

import yaml

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    with open('locators.yaml', 'r') as f:
        locator = yaml.safe_load(f)

    dict_locator = {}
    for item in locator["xpath"]:
        dict_locator[item] = (By.XPATH, locator['xpath'][item])
        print(dict_locator[item])

    # На текущий момент селекторы не реализовано
    # for item in locator["css"]:
    #     dict_locator[item] = (By.CSS_SELECTOR, locator['css'][item])
    #     print(dict_locator[item])


class OperationsHelper(BasePage):

    def enter_login(self, word):
        login_field = self.find_element(TestSearchLocators.dict_locator['LOCATOR_INPUT_USERNAME'])
        login_field.clear()
        login_field.send_keys(word)

    def enter_password(self, word):
        password_field = self.find_element(TestSearchLocators.dict_locator['LOCATOR_INPUT_PASSWORD'])
        password_field.clear()
        password_field.send_keys(word)

    def enter_button(self):
        button_field = self.find_element(TestSearchLocators.dict_locator['LOCATOR_BUTTON_LOGIN'])
        button_field.click()

    def enter_link(self):
        link_field = self.find_element(TestSearchLocators.dict_locator['LOCATOR_LINK_CONTACT'])
        link_field.click()

    def enter_name(self, name):
        name_field = self.find_element(TestSearchLocators.dict_locator['LOCATOR_INPUT_NAME'])
        name_field.clear()
        name_field.send_keys(name)

    def enter_email(self, email):
        email_field = self.find_element(TestSearchLocators.dict_locator['LOCATOR_INPUT_NAME'])
        email_field.clear()
        email_field.send_keys(email)

    def enter_content(self, content):
        content_field = self.find_element(TestSearchLocators.dict_locator['LOCATOR_TEXTAREA_CONTENT'])
        content_field.clear()
        content_field.send_keys(content)

    def enter_contact_us(self):
        contact_us_field = self.find_element(TestSearchLocators.dict_locator['LOCATOR_BUTTON_CONTACT_US'])
        contact_us_field.click()
