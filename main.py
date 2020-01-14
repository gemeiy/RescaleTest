import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import getpass
from selenium.common.exceptions import NoSuchElementException
from BaseClass import BaseTest
import WinFolderFile

#main for tests

class TestRescale(BaseTest):

    def getPage(self):
        self.driver.get("https://platform.rescale.com/jobs/new-job/setup/input-files/")

    def testUploadFile(self, myFilePath):
        self.driver.find_element_by_xpath("//span[contains(text(),'New Job')]").click()
        #self.driver.find_element_by_xpath("//div[@class='rescale-blue b input-from-computer']").click()
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='rescale-blue b input-from-computer']")))
        element.click();

        #open dialog windows to upload a file
        myFileName = WinFolderFile.OpenWin(myFilePath)

        assert self.driver.find_element_by_xpath("//div[@class='ml2']").text == myFileName

    def testNewJob(self):  #test case 1
        #driver = self.driver

        self.getPage()
        try:  #in case login is required
            login = self.driver.find_element_by_xpath("//input[@class='active-input']")
            login.send_keys("gemeiy@gmail.com")
            #nextI = self.driver.find_element_by_xpath("//div[@class='next-step ready']/*[name()='svg']")
            nextI = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='next-step ready']/*[name()='svg']")))
            nextI.click()
            time.sleep(2)
            passwd = self.driver.find_element_by_xpath("//input[@class='active-input']")
            passwd.send_keys("myRescale_0")
            time.sleep(2)
            #loginB = self.driver.find_element_by_xpath("//button[@class='input-link']")
            loginB = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='input-link']")))
            loginB.click()
        except NoSuchElementException as okToPass:
            pass #if the login already omitted by cookies

        userName = getpass.getuser()
        myFilePath = "C:\\Users\\" + userName + "\\Downloads\\airfoil2D.zip"
        self.testUploadFile(myFilePath)  #upload the file from local drive and verify that the file name is loaded in rescale system

        self.quit() #only one test, quit now

myTest = TestRescale()
myTest.testNewJob()
