import time

from Common.logger import Log
from PageLocators.BaiduSearchImage.results_page_locator import ResultsPageLocator as results_locator
from Common.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException

log = Log()
class ResultsPage(BasePage):

    doc = "ImageDetailsPage"
    def get_search_results_image_cols(self):
        log.info("Step: {} - get search results image colunms".format(self.doc))
        try:
            image_cols = self.get_elements(results_locator.search_result_image_col,
                                            self.doc)
            return image_cols
        except:
            log.error("Error occurs!")
            raise

    def get_image_at_position(self, position, max_swipe_up_times):
        log.info("Step: {} - get image element at the position {} within max swipe up times {}".format(self.doc, position, max_swipe_up_times))
        current_swipe_up_time = 0
        image_locator = results_locator().get_image_locator_at_position(position)
        image = None
        while current_swipe_up_time < max_swipe_up_times:
            log.info("Try to find the element in the current page")
            try:
                self.wait_elevisible(image_locator)
                image = self.get_element(image_locator, self.doc)
                break
            except:
                log.info("Cannot find the element in the current page")
                current_swipe_up_time = current_swipe_up_time + 1
                self.swipe_up()
                continue

        if image is None:
            error_message = "Cannot find the image at the position {} within {} swipe up times ".format(position,
                                                                                                             max_swipe_up_times)
            log.error(error_message)
            raise Exception(error_message)
        else:
            return image

    def get_guess_word(self):
        log.info("Step: {} - get guess word based on the input image".format(self.doc))

        guess_word=self.get_element_attribute(results_locator.guess_word_div, "innerText", doc= self.doc)
        return guess_word





