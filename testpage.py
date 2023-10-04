from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    # По какому принципу давались имена константам:
    # СУЩНОСТЬ/ТИП ОБЪЕКТА/НАЗВАНИЕ НА ФРОНТЕ
    LOCATOR_INPUT_USERNAME = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_INPUT_PASSWORD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_BUTTON_LOGIN = (By.XPATH, '''//*[@id="login"]/div[3]/button''')
    LOCATOR_LINK_CONTACT = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[2]/a''')
    LOCATOR_INPUT_NAME = (By.XPATH, '''//*[@id="contact"]/div[1]/label/input''')
    LOCATOR_INPUT_EMAIL = (By.XPATH, '''//*[@id="contact"]/div[2]/label/input''')
    LOCATOR_TEXTAREA_CONTENT = (By.XPATH, '''//*[@id="contact"]/div[3]/label/span/textarea''')
    LOCATOR_BUTTON_CONTACT_US = (By.XPATH, '''//*[@id="contact"]/div[4]/button''')


class OperationsHelper(BasePage):

    def enter_login(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_USERNAME)
        login_field.clear()
        login_field.send_keys(word)

    def enter_password(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_PASSWORD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_button(self):
        login_field = self.find_element(TestSearchLocators.LOCATOR_BUTTON_LOGIN)
        login_field.click()

    def enter_link(self):
        link_field = self.find_element(TestSearchLocators.LOCATOR_LINK_CONTACT)
        link_field.click()

    def enter_name(self, name):
        name_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_NAME)
        name_field.clear()
        name_field.send_keys(name)

    def enter_email(self, email):
        email_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_EMAIL)
        email_field.clear()
        email_field.send_keys(email)

    def enter_content(self, content):
        content_field = self.find_element(TestSearchLocators.LOCATOR_TEXTAREA_CONTENT)
        content_field.clear()
        content_field.send_keys(content)

    def enter_contact_us(self):
        login_field = self.find_element(TestSearchLocators.LOCATOR_BUTTON_CONTACT_US)
        login_field.click()
