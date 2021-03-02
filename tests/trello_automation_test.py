
"""This method implements Python Selenium Unit Test"""

import os
import sys
path = os.path.abspath('..')
sys.path.append(path)

from selenium import webdriver
from pages.loginpage import LoginPage
from pages.boardspage import BoardsPage
from pages.homepage import HomePage
from locators.locators import Locators
from config.config import ConfigTestData

import unittest
import HtmlTestRunner

class TrelloAutomationUnittest(unittest.TestCase):

    """Trello Automation unit test class"""

    @classmethod
    def setUpClass(cls) -> None:

        print("Test started")
        if ConfigTestData.BROWSER == 'Chrome':
            cls.driver = webdriver.Chrome(executable_path=ConfigTestData.CHROME_EXECUTABLE_PATH)

        if ConfigTestData.BROWSER == 'Firefox':
            cls.driver = webdriver.Firefox(executable_path=ConfigTestData.FIREFOX_EXECUTABLE_PATH)

        cls.driver.maximize_window()
        cls.driver.get(ConfigTestData.URL)
        cls.driver.implicitly_wait(10)

    def setUp(self) -> None:
        self.driver.get(ConfigTestData.URL)
        self.loginpage = LoginPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.boardspage = BoardsPage(self.driver)

    def test_01_page_logo(self):
        logo_status = self.loginpage.validate_login_page_logo()
        self.assertEqual(logo_status, True, "Trello icon not found in the page")

    def test_02_login_page_title(self):
        title = self.loginpage.get_login_page_title(Locators.LOGIN_PAGE_TITLE)
        self.assertEqual(Locators.LOGIN_PAGE_TITLE, title, "Title is not matching with Trello page")

    def test_03_invalid_login(self):
        title = self.loginpage.get_login_page_title(Locators.LOGIN_PAGE_TITLE)
        assert Locators.LOGIN_PAGE_TITLE == title, "title not matching"
        status = self.loginpage.invalid_login(ConfigTestData.INVALID_USERNAME, ConfigTestData.INVALID_PASSWORD)
        self.assertEqual(status, True, "Invalid login test execution is failed")

    def test_04_valid_login(self):
        title = self.loginpage.get_login_page_title(Locators.LOGIN_PAGE_TITLE)
        assert Locators.LOGIN_PAGE_TITLE == title, "title not matching"
        status = self.loginpage.valid_login(ConfigTestData.USERNAME, ConfigTestData.PASSWORD)
        self.assertEqual(status, True, "Valid Login test execution is failed")

    def test_05_create_boards(self):
        page_status = self.homepage.validate_home_page_boards_element()
        assert page_status is True, "Login failed"
        status = self.homepage.create_new_board(ConfigTestData.BOARD_NAME)
        self.assertEqual(status, True, "Create boards failed")

    def test_06_create_lists(self):
        self.homepage.search_created_board(ConfigTestData.BOARD_NAME)
        create_list_status = self.boardspage.create_list(Locators.CREATE_LIST_TITLES)
        self.assertEqual(create_list_status, True, "Create list failed")

    def test_07_add_cards(self):
        self.homepage.search_created_board(ConfigTestData.BOARD_NAME)
        create_card_status = self.boardspage.add_cards_to_list_not_started(Locators.CREATE_CARDS_LIST)
        self.assertEqual(create_card_status, True, "Create card failed")

    def test_08_move_cards(self):
        self.homepage.search_created_board(ConfigTestData.BOARD_NAME)
        status1 = self.boardspage.move_card2_to_inprogress()
        status2 = self.boardspage.move_card3_to_QA()
        status3 = self.boardspage.move_card2_to_QA()
        move_cards_status = status1 and status2 and status3
        self.assertEqual(move_cards_status, True, "move cards failed")

    def test_09_assign_user(self):
        self.homepage.search_created_board(ConfigTestData.BOARD_NAME)
        assign_status = self.boardspage.assign_card1_to_current_logged_user(ConfigTestData.LOGGED_USER)
        self.assertEqual(assign_status, True, "assign user failed")

    def test_10validate_logout(self):
        logout_status = self.loginpage.validate_logout_successful()
        self.assertEqual(logout_status, True, "Trello webpage logout failed")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    path = os.path.join(os.path.abspath('..'), 'reports')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\reports", report_name="TestReport",
                                                           report_title="Test Result", combine_reports=True))