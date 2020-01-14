
from selenium import webdriver

class BaseTest(object):

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\temp\\chromedriver.exe")


    def quit(self):  #only call once
        self.driver.quit()


    def close(self):
        self.driver.close()
