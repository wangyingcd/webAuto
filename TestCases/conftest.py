import pytest, time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Common.test_config import TestConfig
from Common.file_config import FileConfig
from Common.logger import Log

log = Log()


@pytest.fixture(scope="class")
def access_web(load_test_config):
    log.info("Class level Setup: Access Web ...")
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome()
    driver.get("https://baidu.com/")
    driver.maximize_window()
    time.sleep(4)
    log.info("Class level Setup: Access Web Done")
    yield load_test_config, driver
    log.info("Class level Cleanup")
    log.info("Class level Cleanup: Save the last visited page")
    driver.save_screenshot(FileConfig().get_path(type="screenshots") + '/' + "last_step_screenshot.png")
    log.info("Class level Cleanup: quit browser")
    driver.quit()


@pytest.fixture(scope="class")
def load_test_config():
    log.info("Class level Setup: Load Test Config ...")
    test_config = TestConfig()
    log.info("Class level Setup: Load Test Config Done")
    yield test_config


def pytest_configure(config):
    config.addinivalue_line("markers", 'smoke')
    config.addinivalue_line("markers", 'P0')
    config.addinivalue_line("markers", 'P1')
