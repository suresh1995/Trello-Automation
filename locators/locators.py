"""This module is used to declare all the page element locators"""

from selenium.webdriver.common.by import By

class Locators:

    """This class contains all the element locators of the Trello webpage"""

    # Login page locators

    LOGIN_PAGE_TITLE = "Trello"
    TRELLO_ICON = (By.XPATH, "//a[@class='d-block float-left']")
    LOGIN_BUTTON_LINK_TEXT = (By.LINK_TEXT, "Log in")
    USERNAME_TEXTBOX_ID = (By.ID, "user")
    PASSWORD_TEXTBOX_ID = (By.ID, "password")
    LOGIN_BUTTON_ID = (By.ID, "login")
    LOGIN_BUTTON_ATTRIBUTE = 'value'
    LOGIN_BUTTON_TEXT = "Log in with Atlassian"
    LOGIN_SUBMIT_BUTTON_ID = (By.ID, "login-submit")

    LOGIN_PAGE_HEADER = (By.XPATH, '/html/body/div[1]/section/div/div/h1')
    LOGIN_PAGE_HEADER_TEXT = "Log in to Trello"

    INVALID_LOGIN_ERROR_MESSAGE = "There isn't an account for this email"
    INVALID_LOGIN_ERROR_MESSAGE_LOCATOR = (By.ID, "error")

    # Home Page Locator

    BOARDS_DASHBOARD = (By.XPATH, "//span[@class='MEu8ZECLGMLeab']")
    BOARDS_TEXT = "Boards"

    CREATE_BOARD_PLUS_BUTTON = (By.XPATH, "//button[@aria-label='Create Board or Team']")
    CREATE_BOARD_BUTTON = (By.XPATH, "//button[@data-test-id='header-create-board-button']")

    ADD_BOARD_TITLE_INPUT_BOX = (By.XPATH, "//input[@aria-label='Add board title']")
    CREATE_BOARD_SUBMIT_BUTTON = (By.XPATH, "//button[@data-test-id='create-board-submit-button']")

    SEARCH_BOARDS = (By.XPATH, '//input[@name="search-boards"]')

    # Boards Page Locator

    BOARD_HEADER_BOX = (By.XPATH, "//input[@class='board-name-input js-board-name-input']")
    BOARD_HEADER_BOX_ATTRIBUTE = 'value'
    BOARD_MENU_WINDOW_CLOSE_BUTTON = (By.XPATH, "//a[@title='Close the board menu.']")

    ADD_LIST_ELEMENT = (By.XPATH, "//span[contains(text(), 'Add a list')]")
    LIST_TITLE_BOX = (By.XPATH, "//input[@name='name']")
    ADD_LIST_BUTTON = (By.XPATH, "//input[@value='Add List']")

    THREE_DOT_ELEMENT = (By.XPATH, "//a[@class='list-header-extras-menu dark-hover js-open-list-menu icon-sm icon-overflow-menu-horizontal']")
    ARCHIVE_LIST = (By.XPATH, "//a[contains(text(),'Archive This List')]")

    CREATE_LIST_TITLES = ['Not Started', 'In Progress', 'QA', 'Done']
    LIST_TEXT_BOX = (By.XPATH, "//div[@class='list-header js-list-header u-clearfix is-menu-shown']")

    ADD_CARD_ELEMENT = (By.XPATH, "//span[contains(text(),'Add a card')]")
    CARD_TITLE_BOX = (By.XPATH, "//textarea[@placeholder='Enter a title for this card…']")
    ADD_CARD_BUTTON = (By.XPATH, "//input[@value='Add Card']")

    CREATE_CARDS_LIST = ['Card 1', 'Card 2', 'Card 3', 'Card 4']

    SOURCE_LOCATOR_CARD2 = (By.XPATH, "//span[contains(text(),'Card 2')]")
    DESTINATION_LOCATOR_IN_PROGRESS = (By.XPATH, "//textarea[contains(text(),'In Progress')]")

    SOURCE_LOCATOR_CARD3 = (By.XPATH, "//span[contains(text(),'Card 3')]")
    DESTINATION_LOCATOR_QA = (By.XPATH, "//textarea[contains(text(),'QA')]")

    CARD1_LOCATOR = (By.XPATH, "//span[contains(text(),'Card 1')]")
    MEMBERS_BUTTON = (By.XPATH, "//a[@title='Members']")
    SEARCH_MEMBERS_TEXT_BOX = (By.XPATH, "//input[@placeholder='Search members']")
    BOARD_MEMBERS_LIST_ELEMENT = (By.XPATH, "//span[@class='full-name']")
    MEMBERS_WINDOW_CLOSE_BUTTON = (By.XPATH, "//a[@class='pop-over-header-close-btn icon-sm icon-close']")

    COMMENT_BOX = (By.XPATH, "//textarea[@placeholder='Write a comment…']")
    SAVE_BUTTON = (By.XPATH, "//input[@value='Save']")
    CLOSE_WINDOW_ELEMENT = (By.XPATH, "//a[@class='icon-md icon-close dialog-close-button js-close-window']")
    COMMENT_MESSAGE = "I am done"

    ACCOUNT_SETTINGS_ELEMENT_PATH = (By.XPATH, "//div[@class='_1FekJJAz6Hu32v']")
    LOGOUT_BUTTON = (By.XPATH, "//span[contains(text(), 'Log Out')]")

    LOGOUT_ID = (By.ID, "logout-submit")
    LOGOUT_SUCCESS_ELEMENT = (By.XPATH, "/html/body/div[2]/div/h1")
    LOGOUT_SUCCESS_MESSAGE = "Thanks for using Trello."