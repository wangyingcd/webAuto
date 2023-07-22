from selenium.webdriver.common.by import By


class HomePageLocator:
    searchByImageBtn = (By.XPATH, "//span[@class='soutu-btn']")

    uploadImageEle = (By.XPATH, "//input[@class='upload-pic']")
