"""This Class is used to implement methods for Login page"""

from locators.locators import Locators
from pages.basepage import BasePage
import time

class LoginPage(BasePage):

    """This class contains methods to interact with Login page"""

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        """Validate login page title"""
        return self.get_page_title(title)

    def validate_login_page_logo(self):
        """Validate login page logo"""
        return self.is_visible(Locators.TRELLO_ICON)

    def valid_login(self, username, password):
        """checks for Valid login"""
        self.click_element(Locators.LOGIN_BUTTON_LINK_TEXT)
        element_text = self.get_element_text(Locators.LOGIN_PAGE_HEADER)
        time.sleep(2)
        if element_text == Locators.LOGIN_PAGE_HEADER_TEXT:
            self.enter_text(Locators.USERNAME_TEXTBOX_ID, username)
            time.sleep(5)
            login_button_element_attribute = self.get_element_attribute(Locators.LOGIN_BUTTON_ID,
                                                                        Locators.LOGIN_BUTTON_ATTRIBUTE)
            if not self.is_visible(Locators.PASSWORD_TEXTBOX_ID) \
                    and login_button_element_attribute == Locators.LOGIN_BUTTON_TEXT:
                self.click_element(Locators.LOGIN_BUTTON_ID)
                self.enter_text(Locators.PASSWORD_TEXTBOX_ID, password)
                self.click_element(Locators.LOGIN_SUBMIT_BUTTON_ID)
                time.sleep(10)
                self.is_visible(Locators.BOARDS_DASHBOARD)
                time.sleep(5)
                return True
            else:
                return False


    def invalid_login(self, invalid_username, invalid_password):
        """checks for invalid login details"""
        self.click_element(Locators.LOGIN_BUTTON_LINK_TEXT)
        element_text = self.get_element_text(Locators.LOGIN_PAGE_HEADER)
        if element_text == Locators.LOGIN_PAGE_HEADER_TEXT:
            self.enter_text(Locators.USERNAME_TEXTBOX_ID, invalid_username)
            self.enter_text(Locators.PASSWORD_TEXTBOX_ID, invalid_password)
            self.click_element(Locators.LOGIN_BUTTON_ID)
            error_message = self.get_element_text(Locators.INVALID_LOGIN_ERROR_MESSAGE_LOCATOR)
            if error_message == Locators.INVALID_LOGIN_ERROR_MESSAGE:
                return True
            else:
                return False

        else:
            print("Login page is not loaded")
            return False

    def validate_logout_successful(self):
        """validate logout and checks for logout success message"""
        self.click_element(Locators.ACCOUNT_SETTINGS_ELEMENT_PATH)
        self.click_element(Locators.LOGOUT_BUTTON)
        self.click_element(Locators.LOGOUT_ID)
        time.sleep(5)
        element_text = self.get_element_text(Locators.LOGOUT_SUCCESS_ELEMENT)
        if Locators.LOGOUT_SUCCESS_MESSAGE in element_text:
            return True
        return False