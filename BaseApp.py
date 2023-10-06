from logging_config import setup_logging

import yaml
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata['address']
        self.logger = setup_logging()

    def find_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                          message=f"элемент {locator} не найден")
            self.logger.exception("GeekBrains")
        except:
            self.logger.exception("GeekBrains")
            return None

    def get_element_property(self, mode, locator, property):
        element = self.find_element(mode, locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def close(self):
        self.driver.close()
