from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import calendar as cal
from Common.file_config import FileConfig
from Common.logger import Log
import time, datetime
from selenium.webdriver.common.keys import Keys

log = Log()


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_elevisible(self, loc, timeout=120, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        log.info("Try to wait {}'s element {} visible ...".format(doc, loc))

        start_time = time.time()
        try:

            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
        except:
            log.error("Failure: Waiting {}'s element {} timeout".format(doc, loc))
            self.do_save_screenshot(doc)
            raise
        else:
            end_time = time.time()
            duration = end_time - start_time
            log.info("Success: Waiting {}'s element {} visible, duration {}".format(doc, loc, duration))

    def get_element(self, loc, doc=""):
        """
        :param loc:
        :param doc:
        :return:
        """
        log.info("Try to Get {}'s element {} ...".format(doc, loc))

        try:
            ele = self.driver.find_element(*loc)
        except:
            log.error("Failure: Get {}'s element {} failed".format(doc, loc))
            self.do_save_screenshot(doc)
            raise
        else:
            log.info("Success: Get {}'s element {} successfully".format(doc, loc))
            return ele

    def click(self, loc, timeout=8, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        log.info("Try to Click on {}'s element {} ...".format(doc, loc))

        time.sleep(0.5)
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            ele.click()
        except:
            log.error("Failure: Click on {}'s element {} failed".format(doc, loc))
            self.do_save_screenshot(doc)
            raise
        else:
            log.info("Success: Click on {}'s element {} successfully".format(doc, loc))

    def get_elements(self, loc, doc=""):
        """
        :param loc:
        :param doc:
        :return:
        """
        log.info("Try to get {}'s element {} ...".format(doc, loc))
        try:
            self.wait_elevisible(loc)
            ele = self.driver.find_elements(*loc)
        except:
            log.error("Failure: Get {}'s element {} failed".format(doc, loc))
            self.do_save_screenshot(doc)
            raise
        else:
            log.info("Success: Get {}'s element {} successfully".format(doc, loc))
            return ele

    def get_element_attribute(self, loc, attr, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param attr:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            value = ele.get_attribute(attr)
        except:
            log.error("获取{}元素属性值失败".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            log.info("获取{}元素属性值成功".format(loc))
            return value

    def do_save_screenshot(self, doc=""):
        """
        :param doc:
        :return:
        """
        log.info("Try to save screenshot ...")
        cur_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
        # file = screenshot_dir+"/{}_{}.png".format(doc,cur_time)
        file = FileConfig().get_path(type="screenshots") + "/{}_{}.png".format(doc, cur_time)
        try:
            self.driver.save_screenshot(file)
        except:
            log.error("Failure: Save screenshot failed")
        else:
            log.info("Success: Save screenshot successfully. File full path is {}").format(file)

    def switch_window(self, doc=""):
        log.info("Try to switch window ...")
        try:
            # Get the windows list
            windows = self.driver.window_handles
            # Switch to latest opened window
            self.driver.switch_to.window(windows[-1])
        except:
            log.error("Failure: Switching window fails")
            self.do_save_screenshot(doc)
            raise
        else:
            log.info("Success: Switching window successes")

    def input_text_uploadfile(self, loc, value, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param value:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        log.info("Try to upload file {} to {}'s element {} ...".format(value, doc, loc))
        ele = self.get_element(loc, doc)
        try:
            ele.send_keys(value)
        except:
            log.error("Failure: Upload file {} to {}'s element {} failed".format(value, doc, loc))
            self.do_save_screenshot(doc)
            raise
        else:
            log.info("Success: Upload file {} to {}'s element {} successfully".format(value, doc, loc))

    def swipe_up(self):
        log.info("Swipe up 1 time ...")
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(3)
