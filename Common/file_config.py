#!/usr/bin/python3
import os
import platform


class FileConfig:

    def __init__(self):
        self.computer_sys = platform.system()
        self.base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

    def get_path(self, type):
        self.allure_dir = ""
        self.htmlreport_dir = ""
        self.logs_dir = ""
        self.screenshot_dir = ""
        self.testdata_dir = ""

        if platform.system() == "Windows":
            # Windows
            if type == "allure_report":
                self.allure_dir = os.path.join(self.base_dir, "Outputs\\allure_report")
                return self.allure_dir
            elif type == "pytest_report":
                self.htmlreport_dir = os.path.join(self.base_dir, "Outputs\\pytest_report")
                return self.htmlreport_dir
            elif type == "logs":
                self.logs_dir = os.path.join(self.base_dir, "Outputs\\logs")
                return self.logs_dir
            elif type == "screenshots":
                self.screenshot_dir = os.path.join(self.base_dir, "Outputs\\screenshots")
                return self.screenshot_dir
            elif type == "Outputs":
                self.Outputs_dir = os.path.join(self.base_dir, "Outputs")
                return self.Outputs_dir
            elif type == "testdata":
                self.testdata_dir = os.path.join(self.base_dir, "TestData")
                return self.testdata_dir
            else:
                self.message = "type options：allure_report/pytest_report/logs/screenshots/testdata"
                return self.message
        else:
            # Mac OR Linux
            if type == "allure_report":
                self.allure_dir = os.path.join(self.base_dir, "Outputs/allure_report")
                return self.allure_dir
            elif type == "pytest_report":
                self.htmlreport_dir = os.path.join(self.base_dir, "Outputs/pytest_report")
                return self.htmlreport_dir
            elif type == "logs":
                self.logs_dir = os.path.join(self.base_dir, "Outputs/logs")
                return self.logs_dir
                self.screenshot_dir = os.path.join(self.base_dir, "Outputs/screenshots")
                return self.screenshot_dir
            elif type == "Outputs":
                self.Outputs_dir = os.path.join(self.base_dir, "Outputs")
                return self.Outputs_dir
            elif type == "testdata":
                self.testdata_dir = os.path.join(self.base_dir, "TestData")
                return self.testdata_dir
            else:
                self.message = "type选择范围：allure_report/pytest_report/logs/screenshots/Outputs/testdata"
                return self.message


if __name__ == "__main__":
    print(FileConfig().get_path(type="logs"))
