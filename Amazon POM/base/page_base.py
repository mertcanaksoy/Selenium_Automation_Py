from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BaseClass(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def wait_for_element(self, selector):
        """
        Wait for element to present
        :param selcetor: locator of the element to find

        """
        return self.wait.until(EC.element_to_be_clickable(selector))

    def presence_for_element(self, selector):
        """
        Presence for element to present
        :param selector: locator of the element to find

        """
        return self.wait.until(EC.presence_of_element_located(selector))

    def presence_for_all_elements(self, selector):
        """
        Presence for element to present
        :param selector: locator of the elements to find
        :param index: index of selected element

        """
        return self.wait.until(EC.presence_of_all_elements_located(selector))

    def wait_till_element_disappears(self, selector):
        """
        Wait for element to disappears
        :param selector: locator of the element to find

        """
        return self.wait.until(EC.invisibility_of_element_located(selector))

    def exist_element(self, selector, multiple=False):
        """
        Return true if element/elements present and false if element/elements absent
        :param selector: locator of the element to find
        :param multiple: False in default, if True returns the list of WebElements once they are located

        """
        if not multiple:
            try:
                self.wait.until(EC.presence_of_element_located(selector))
                return True
            except TimeoutException:
                return False
        else:
            try:
                self.wait.until(EC.presence_of_all_elements_located(selector))
                return True
            except TimeoutException:
                return False

