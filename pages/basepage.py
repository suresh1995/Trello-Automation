"""This class is the parent base class for all page class"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:

    """This Class is the parent class for the page class in the application"""

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        """"do click operations on the page"""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        except TimeoutException as e:
            print("No element found", e)

    def enter_text(self, by_locator, text):
        """"enter inputs in the text box"""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except TimeoutException as e:
            print("No element found", e)

    def get_element_text(self, by_locator):
        """"get element text"""
        try:
            element_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
            return element_text
        except TimeoutException as e:
            print("No element found", e)

    def get_element_attribute(self, by_locator, attribute):
        """"get element attribute"""
        try:
            element_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).get_attribute(attribute)
            return element_text
        except TimeoutException as e:
            print("No element found", e)

    def get_page_title(self, title):
        """"get tile of the page"""
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
            return self.driver.title
        except TimeoutException:
            print("title not found")

    def is_visible(self, by_locator):
        """"check element is visible in the page"""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def type_text_and_press_enter(self, by_locator, text):
        """"type text and press enter"""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)
        except TimeoutException as e:
            print("No element found", e)

    def drag_and_drop(self, source, destination):
        """"drag and drop element from source to destination"""
        try:
            source = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(source))
            destination = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(destination))
            ActionChains(self.driver).drag_and_drop(source, destination).perform()
        except TimeoutException as e:
            print("No element found", e)
