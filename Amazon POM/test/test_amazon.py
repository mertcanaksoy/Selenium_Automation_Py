import unittest
from amazon_setup import Setup


class AmazonTestCase(unittest.TestCase, Setup):
    """Test Case
        1. Go to http://www.amazon.com and approve to main page opens,
        2. Open the login page, then login with a user,
        3. Write the 'samsung' to searchbox the above of the screen, then click the search button,
        4. Approve the results for Samsung on this page,
        5. Click the 2nd page on Search Results, then approve the page is 2nd page,
        6. Click the inside of  3rd products 'Add to List' button,
        7. Click the 'List' link bottom of the page, then select the Wish list,
        8. Approve the product what it added to wish list,
        9. Click to 'Delete' button,
        10. Approve the product is not available in wish list anymore.
        """

    def setUp(self):
        Setup.__init__(self)

    def test_amazon(self):
        self.amazon_main.navigate_to_home_page()
        self.amazon_main.navigate_to_sign_in()
        self.amazon_login.login()
        self.amazon_main.navigate_to_search_product()
        self.amazon_category.navigate_to_second_page()
        self.amazon_category.click_product()
        self.amazon_product.add_product_to_list()
        self.amazon_product.navigate_to_your_list()
        self.amazon_wishlist.delete_item()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

