from PageLocators.BaiduSearchImage.image_details_page_locator import ImageDetailsPageLocator as details_locator
from Common.base_page import BasePage


class ImageDetailsPage(BasePage):
    doc = "ImageDetailsPage"

    def get_image(self):
        self.switch_window(doc="switch window")
        self.wait_elevisible(details_locator.image, timeout=8, doc=self.doc)
        image = self.get_element(details_locator.image, doc=self.doc)
        return image
