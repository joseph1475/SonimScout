from appium.webdriver.common.mobileby import By

class SonimScoutSetup:
    def __init__(self,driver1):
        self.driver1 = driver1


    setup = (By.XPATH,"//*[@text='Sonim Setup Wizard']")
    #self.driver1.find_element_by_xpath("//*[@text='Sonim Setup Wizard']")
    def ScoutSetup(self):
        return self.driver1.find_element(*SonimScoutSetup.setup)


    btnQuit = (By.ID,"com.sonimtech.setupwizard.ten:id/btnQuit")
    def Quit(self):
        return self.driver1.find_element(*SonimScoutSetup.btnQuit)
    #self.driver1.find_element_by_id("com.sonimtech.setupwizard.ten:id/btnQuit").click()