
"""This Class is used to implement methods for Boards page"""

from locators.locators import Locators
from pages.basepage import BasePage
import time

class BoardsPage(BasePage):

    """This class contains methods to interact with Boards page"""

    def __init__(self, driver):
        self.driver = driver

    def create_list(self, create_list_titles):
        """"create lists in the board"""

        while self.is_visible(Locators.THREE_DOT_ELEMENT):
            self.archive_list()

        self.is_visible(Locators.ADD_LIST_ELEMENT)
        self.click_element(Locators.ADD_LIST_ELEMENT)
        time.sleep(5)
        for list_title in create_list_titles:
            self.enter_text(Locators.LIST_TITLE_BOX, list_title)
            self.click_element(Locators.ADD_LIST_BUTTON)
            time.sleep(2)
        self.is_visible(Locators.BOARD_MENU_WINDOW_CLOSE_BUTTON)
        self.click_element(Locators.BOARD_MENU_WINDOW_CLOSE_BUTTON)
        return True

    def archive_list(self):
        """archive list from the board"""
        self.is_visible(Locators.THREE_DOT_ELEMENT)
        self.click_element(Locators.THREE_DOT_ELEMENT)
        self.click_element(Locators.ARCHIVE_LIST)

    def add_cards_to_list_not_started(self, cards_list):
        """"add cards to not started list"""
        self.is_visible(Locators.ADD_CARD_ELEMENT)
        self.click_element(Locators.ADD_CARD_ELEMENT)
        for card_name in cards_list:
            self.enter_text(Locators.CARD_TITLE_BOX, card_name)
            self.click_element(Locators.ADD_CARD_BUTTON)
            time.sleep(2)
        return True

    def move_card2_to_inprogress(self):
        """"move card2 to inprogress"""
        self.drag_and_drop(Locators.SOURCE_LOCATOR_CARD2, Locators.DESTINATION_LOCATOR_IN_PROGRESS)
        time.sleep(2)
        return True

    def move_card3_to_QA(self):
        """"move card3 to QA"""
        self.drag_and_drop(Locators.SOURCE_LOCATOR_CARD3, Locators.DESTINATION_LOCATOR_QA)
        time.sleep(2)
        return True

    def move_card2_to_QA(self):
        """"move card2 to QA"""
        self.drag_and_drop(Locators.SOURCE_LOCATOR_CARD2, Locators.DESTINATION_LOCATOR_QA)
        time.sleep(2)
        return True

    def assign_card1_to_current_logged_user(self, user):
        """"assign card1 to current logged user"""
        self.click_element(Locators.CARD1_LOCATOR)
        self.click_element(Locators.MEMBERS_BUTTON)
        self.enter_text(Locators.SEARCH_MEMBERS_TEXT_BOX, user)
        time.sleep(2)
        element_text = self.get_element_text(Locators.BOARD_MEMBERS_LIST_ELEMENT)
        if user in element_text:
            self.click_element(Locators.BOARD_MEMBERS_LIST_ELEMENT)
            self.click_element(Locators.MEMBERS_WINDOW_CLOSE_BUTTON)

        self.enter_text(Locators.COMMENT_BOX, Locators.COMMENT_MESSAGE)
        self.click_element(Locators.SAVE_BUTTON)
        self.click_element(Locators.CLOSE_WINDOW_ELEMENT)
        time.sleep(2)
        return True