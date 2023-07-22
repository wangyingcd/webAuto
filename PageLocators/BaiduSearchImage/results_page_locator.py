import string
from selenium.webdriver.common.by import By


class ResultsPageLocator:
    search_result_image_col = (By.XPATH, "//div[@class='general-imgcol']")

    image_in_position_xpath_str = "//a[@class='general-imgcol-item' and @data-index='{}']/img"

    guess_word_div = (By.XPATH, "//div[@class='graph-guess-word']")

    def get_image_locator_at_position(self, position):
        return By.XPATH, self.image_in_position_xpath_str.format(position - 1)
