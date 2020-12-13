import pytest
from utilities.BaseClass import BaseClass
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



class TestRestrictFeatures(BaseClass):
    '''desired_capsContacts = {
        "automationName": "UiAutomator2",  # Appium (default), or UiAutomator2
        "platformName": "Android",  # Andriod,IOS
        "platformVersion": "",  # can be open type or can declare the version .Eg: 8.1.1
        "deviceName": "903890ef",  # Android Emulator or 903e900a device ID
        "appPackage": "com.android.contacts",
        "appActivity": "com.android.contacts.activities.PeopleActivity"
    }'''

    def test_pincode(self):
        self.verifyElementPresence("//*[@text='SafeGuard']")
        self.driver1.find_element_by_xpath("//android.widget.TextView[@text='SafeGuard']").click()
        self.driver1.find_element_by_class_name("android.widget.Switch").click()
        self.driver1.find_element_by_class_name("android.widget.EditText").send_keys(1234)
        time.sleep(5)
        self.driver1.find_element_by_id("android:id/button1").click()
        self.driver1.find_element_by_xpath("//*[@text='Features']").click()
        inputpin = self.driver1.find_element_by_xpath("//*[@text ='Input PIN']").text
        assert inputpin == "Input PIN"

    def test_ListofApps(self):
        self.driver1.find_element_by_class_name("android.widget.EditText").send_keys(1234)
        self.driver1.find_element_by_id("android:id/button1").click()
        SonimRestrictedFeatureList = len(self.driver1.find_elements_by_id("com.sonim.safeguard:id/app_name"))
        count = 0
        count = count + SonimRestrictedFeatureList
        for i in range(SonimRestrictedFeatureList):
            AppsName = (self.driver1.find_elements_by_id("com.sonim.safeguard:id/app_name")).__getitem__(i).text
            time.sleep(1)
            print(AppsName)
        #action.press(x=750, y=1750).move_to(x=0, y=-75).perform()
        print(count)
        assert count == 9

    def test_selectall(self):
        self.driver1.find_element_by_xpath("//android.widget.ImageButton[contains(@index, '2')]").click()
        self.driver1.find_element_by_xpath("//*[@text ='Select All']").click()
        count = 0
        # adjust here to your needs !
        #for x in range(0, 4):
            #wait.until(expected_conditions.presence_of_all_elements_located((By.ID, "com.sonim.safeguard:id/app_name")))
        '''SonimRestricteFeatureList = len(self.driver1.find_elements_by_id("com.sonim.safeguard:id/app_name"))
        checkbox = len(self.driver1.find_element_by_android_uiautomator("new UiSelector().checked(true)"))
            #count = count + SonimRestricteFeatureList
        for i in range(SonimRestricteFeatureList):
            checkbox =len( self.driver1.find_element_by_android_uiautomator("new UiSelector().checked(true)"))
            #if checkbox == "false":
            count = count + 1
            time.sleep(1)
        print(count)
        assert checkbox == 9
        self.driver1.press_keycode(4)'''

    def test_canceloption(self):
        self.driver1.find_element_by_xpath("//*[@text ='CANCEL']").click()
        activation = self.driver1.find_element_by_xpath("//*[@text = 'Activation']").text
        print(activation)
        assert activation == "Activation"

    def test_discardmsg(self):
        self.driver1.find_element_by_xpath("//android.widget.ImageButton[contains(@index, '2')]").click()
        self.driver1.find_element_by_xpath("//*[@text ='Select All']").click()
        self.driver1.press_keycode(4)
        discardMsg = self.driver1.find_element_by_id('android:id/message').text
        if discardMsg == "Do you really want to discard these changes?":
            print("popup displayed")
            self.driver1.find_element_by_xpath("//*[@text = 'OK']").click()
        activation = self.driver1.find_element_by_xpath("//*[@text = 'Activation']").text
        print(activation)
        assert activation == "Activation"

    def test_unselectall(self):
        self.driver1.find_element_by_xpath("//*[@text='Features']").click()
        self.driver1.find_element_by_class_name("android.widget.EditText").send_keys(1234)
        self.driver1.find_element_by_id("android:id/button1").click()
        self.driver1.find_element_by_xpath("//android.widget.ImageButton[contains(@index, '2')]").click()
        self.driver1.find_element_by_xpath("//*[@text ='Select All']").click()
        self.driver1.find_element_by_xpath("//android.widget.ImageButton[contains(@index, '2')]").click()
        self.driver1.find_element_by_xpath("//*[@text ='Unselect All']").click()
        '''count2 = 0
        # adjust here to your needs !
        #for x in range(0, 4):
            #wait.until(expected_conditions.presence_of_all_elements_located((By.ID, "com.sonim.safeguard:id/app_name")))
        SonimRestricteFeatureList = len(self.driver1.find_elements_by_id("com.sonim.safeguard:id/app_name"))
            #count = count + SonimRestricteFeatureList
        for i in range(SonimRestricteFeatureList):
            checkbox = self.driver1.find_element_by_android_uiautomator("new UiSelector().checked(true)")
            if checkbox == "false":
                count2 = count2 + 1
                time.sleep(1)
        print(count2)
        assert count2 == 9
        self.driver1.press_keycode(4) '''

    def test_saveoption(self):
        self.driver1.find_element_by_xpath("//*[@text='Modify Contacts']").click()
        self.driver1.find_element_by_xpath("//*[@text='SAVE']").click()
        '''Contactsdriver = self.webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capsContacts)
        Contactsdriver.find_element_by_id("com.sonim.safeguard:id/editText").send_keys(1234)'''