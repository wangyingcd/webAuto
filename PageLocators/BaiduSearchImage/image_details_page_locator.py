from selenium.webdriver.common.by import By


class ImageDetailsPageLocator:
    image = (By.XPATH, "//div[@class='page-similar-big-cont']/child::a/child::img")
