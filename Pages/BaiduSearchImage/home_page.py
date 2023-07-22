import time

from PageLocators.BaiduSearchImage.home_page_locator import HomePageLocator as HP
from Common.base_page import BasePage
from Common.file_config import FileConfig
from Common.logger import Log

log = Log()


class HomePage(BasePage):
    doc = "BaiduHomePage"

    def search_by_image(self, image_name):
        log.info("Step: HomePage- search by image")

        self.click(HP.searchByImageBtn, doc=self.doc)
        file_fullpath = FileConfig().get_path(type="testdata") + "/" + image_name
        self.input_text_uploadfile(HP.uploadImageEle, file_fullpath, doc=self.doc)
        # ele = self.get_element(HP.uploadImageEle)
        # ele.send_keys()
