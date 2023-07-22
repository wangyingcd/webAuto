import pytest, allure

from Pages.BaiduSearchImage.home_page import HomePage
from Pages.BaiduSearchImage.results_page import ResultsPage
from Pages.BaiduSearchImage.image_details_page import ImageDetailsPage
from Common.logger import Log
from Common.test_config import TestConfig
from Common import test_config
import time

log = Log()


@allure.feature("")
class TestChannel:

    @pytest.mark.P0
    @allure.story("Search by Image ")
    def test_search_by_image(self, access_web):
        log.info("---------------Start Test Case---------------")
        log.info("Start getting the test config")
        config = access_web[0]
        visit_result_position = config.test_config_dic[test_config.global_config_keys[0]]
        max_swipe_times = config.test_config_dic[test_config.global_config_keys[1]]
        image_name = config.test_config_dic[test_config.global_config_keys[2]]
        expected_keyword = config.test_config_dic[test_config.global_config_keys[3]]
        log.info("Complete getting the test config")
        home_page = HomePage(access_web[1])
        result_page = ResultsPage(access_web[1])
        details_page = ImageDetailsPage(access_web[1])

        home_page.search_by_image(image_name)
        image_cols = result_page.get_search_results_image_cols()
        log.info("Check if any result is returned")
        assert (len(image_cols) > 0, "No search result is rendered")

        log.info("Validation: validate the search result image is related with the input image")
        actual_guessWord = result_page.get_guess_word()
        assert (expected_keyword in actual_guessWord,
                "Failure: The guess word {} is not match with expected {}".format(actual_guessWord, expected_keyword))

        image = result_page.get_image_at_position(visit_result_position, max_swipe_times)
        img_src = image.get_attribute('src')

        log.info("Visit the search result at the position {}".format(visit_result_position))
        image.click()
        time.sleep(2)
        # Check image in the image details page
        image_detailsPage = details_page.get_image()
        image_src_detailsPage = image_detailsPage.get_attribute('src')
        assert (img_src == image_src_detailsPage, "Failure: The images are NOT match in results and image details page")
        log.info("---------------Test case ends---------------")
