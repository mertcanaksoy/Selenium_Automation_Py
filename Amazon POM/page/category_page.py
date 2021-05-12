from selenium.webdriver.common.by import By
from base.page_base import BaseClass

class AmazonCategoryPage:
    """ Category Page Operations """

    PAGINATION_CATEGORY = (By.XPATH, '//li[@class="a-normal"]')
    CLICK_PRODUCT = (By.CSS_SELECTOR, '.s-result-item .sg-col-inner')
    IS_SECOND_CATEGORY_PAGE = (By.XPATH, '//span[contains(text(),"17-32")]')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def navigate_to_second_page(self):
        """ Navigate to 2. category page """
        self.methods.presence_for_all_elements(self.PAGINATION_CATEGORY)[0].click()
        assert self.methods.wait_for_element(self.IS_SECOND_CATEGORY_PAGE).is_displayed(), "2. Page Has Been Shown"

    def click_product(self):
        """ Click product and navigate to product detail page """
        self.methods.presence_for_all_elements(self.CLICK_PRODUCT)[1].click()