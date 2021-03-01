
"""This Class is used to implement methods for Home page"""

from pages.basepage import BasePage
from locators.locators import Locators
import time

class HomePage(BasePage):

    """This class contains methods to interact with Home page"""

    def __init__(self, driver):
        super().__init__(driver)

    def validate_home_page_boards_element(self):
        """"validate home page board element"""
        self.is_visible(Locators.BOARDS_DASHBOARD)
        if self.get_element_text(Locators.BOARDS_DASHBOARD) == Locators.BOARDS_TEXT:
            print("Login Successful")
            return True
        else:
            return False

    def create_new_board(self, board_name):
        """"to create new board"""
        self.click_element(Locators.CREATE_BOARD_PLUS_BUTTON)
        self.click_element(Locators.CREATE_BOARD_BUTTON)
        self.enter_text(Locators.ADD_BOARD_TITLE_INPUT_BOX, board_name)
        self.is_visible(Locators.CREATE_BOARD_SUBMIT_BUTTON)
        self.click_element(Locators.CREATE_BOARD_SUBMIT_BUTTON)
        time.sleep(5)
        return True

    def search_created_board(self, board_name):
        """"to search created board"""
        self.is_visible(Locators.BOARDS_DASHBOARD)
        self.click_element(Locators.BOARDS_DASHBOARD)
        self.type_text_and_press_enter(Locators.SEARCH_BOARDS, board_name)
        time.sleep(5)