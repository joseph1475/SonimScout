import pytest
from utilities.BaseClass import BaseClass
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

'''Whatsapp should be installed in the device'''


class TestScout(BaseClass):

    '''def test_ListofApplications(self):
        self.driver1.find_element_by_xpath("//*[@text='SafeGuard']").click()
        self.driver1.find_element_by_id("com.sonim.safeguard:id/switch_widget").click
        self.driver1.find_element_by_id("com.sonim.safeguard:id/dialog_edit_text").send_keys(1234)
        self.driver1.find_element_by_id("android:id/button1").click()
        self.driver1.find_element_by_xpath("//*[@text='Applications']").click()
        self.driver1.find_element_by_id("com.sonim.safeguard: id / dialog_edit_text").send_keys(1234)
        self.driver1.find_element_by_id("android:id/button1").click()
        SonimRestrictedAppsList = len(self.driver1.find_elements_by_id("com.sonim.safeguard:id/app_name"))
        for i in range(SonimRestrictedAppsList):
            AppsName = (self.driver1.find_elements_by_id("com.sonim.safeguard:id/app_name")).__getitem__(i).text
            print(AppsName)'''

    def test_CancelOption(self):
        self.driver1.find_element_by_xpath("//android.widget.TextView[@text='SafeGuard']").click()
        self.driver1.find_element_by_class_name("android.widget.Switch").click()
        self.driver1.find_element_by_class_name("android.widget.EditText").send_keys(1234)
        time.sleep(5)
        self.driver1.find_element_by_id("android:id/button1").click()
        self.driver1.find_element_by_xpath("//*[@text='Applications']").click()
        self.driver1.find_element_by_class_name("android.widget.EditText").send_keys(1234)
        self.driver1.find_element_by_id("android:id/button1").click()
        self.driver1.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()."
            "resourceId(\"android:id/list\"))."
            "scrollIntoView(new UiSelector()."
            "textMatches(\"Contacts\")."
            "instance(0))")
        time.sleep(5)
        self.driver1.find_element_by_xpath("//*[@text='Contacts']").click()
        self.driver1.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()."
            "resourceId(\"android:id/list\"))."
            "scrollIntoView(new UiSelector()."
            "textMatches(\"WhatsApp\")."
            "instance(0))")
        time.sleep(5)
        self.driver1.find_element_by_xpath("//*[@text='WhatsApp']").click()
        self.driver1.find_element_by_xpath("//*[@text='CANCEL']").click()
        activation = self.driver1.find_element_by_xpath("//*[@text = 'Activation']").text
        print(activation)
        assert activation == "Activation"

    def test_Selectall(self):
        action = TouchAction(self.driver1)
        wait = WebDriverWait(self.driver1, 5)
        self.driver1.find_element_by_xpath("//*[@text='Applications']").click()
        self.driver1.find_element_by_class_name("android.widget.EditText").send_keys(1234)
        self.driver1.find_element_by_id("android:id/button1").click()
        self.driver1.find_element_by_xpath("//android.widget.ImageButton[contains(@index, '2')]").click()
        self.driver1.find_element_by_xpath("//*[@text ='Select All']").click()
        count = 0
        # adjust here to your needs !
        for x in range(0,4):
            wait.until(expected_conditions.presence_of_all_elements_located((By.ID, "com.sonim.safeguard:id/app_name")))
            SonimRestrictedAppsList = len(self.driver1.find_elements_by_id("com.sonim.safeguard:id/app_name"))
            count = count + SonimRestrictedAppsList
            for i in range(SonimRestrictedAppsList):
                checkbox = self.driver1.find_element_by_android_uiautomator("new UiSelector().checked(true)")
                if checkbox == "false":
                    count = count+1
                    time.sleep(1)
            action.press(x=750, y=1750).move_to(x=0, y=-75).perform()
        print(count)
        assert count == 35
        self.driver1.press_keycode(4)

    def test_discardmsg(self):
        discardMsg = self.driver1.find_element_by_id('android:id/message').text
        if discardMsg == "Do you really want to discard these changes?":
            print("popup displayed")
            self.driver1.find_element_by_xpath("//*[@text = 'OK']").click()
        activation = self.driver1.find_element_by_xpath("//*[@text = 'Activation']").text
        print(activation)
        assert activation == "Activation"

    def test_Unselectall(self):
        count = 0
        self.driver1.find_element_by_xpath("//*[@text='Applications']").click()
        self.driver1.find_element_by_class_name("android.widget.EditText").send_keys(1234)
        self.driver1.find_element_by_id("android:id/button1").click()
        upaction = TouchAction(self.driver1)
        self.driver1.find_element_by_xpath("//android.widget.ImageButton[contains(@index, '2')]").click()
        self.driver1.find_element_by_xpath("//*[@text ='Select All']").click()
        self.driver1.find_element_by_xpath("//android.widget.ImageButton[contains(@index, '2')]").click()
        self.driver1.find_element_by_xpath("//*[@text ='Unselect All']").click()
        count2=0
        for x in range(0,4):
            #self.wait.until(expected_conditions.presence_of_all_elements_located((By.ID, "com.sonim.safeguard:id/app_name")))
            SonimRestrictedAppsList = len(self.driver1.find_elements_by_id("com.sonim.safeguard:id/app_name"))
            count = count + SonimRestrictedAppsList
            for i in range(SonimRestrictedAppsList):
                checkbox = self.driver1.find_element_by_android_uiautomator("new UiSelector().checked(false)")
                if checkbox == "false":
                    count2 = count2+1
                    time.sleep(1)
            upaction.press(x=750, y=1750).move_to(x=0, y=-75).perform()
        print(count2)
        #assert count2 == 35

    def test_Searchapps(self):
        self.driver1.find_element_by_xpath("//*[@text ='Search applications']").send_keys("Photos")
        photosApp = self.driver1.find_element_by_xpath("//*[@text ='Photos']").text
        if photosApp == "Photos":
            print("success")
        assert photosApp == "Photos"
        self.driver1.press_keycode(4)
        self.driver1.find_element_by_xpath("//*[@text = 'OK']").click()


    def test_wrongpin(self):
        self.driver1.find_element_by_class_name("android.widget.Switch").click()
        self.driver1.find_element_by_class_name("android.widget.EditText").send_keys(4321)
        self.driver1.find_element_by_xpath("//*[@text ='Enter PIN here']").click()
        wrongpin_text =self.driver1.find_element_by_xpath("//*[@text ='Input PIN]").text
        assert wrongpin_text == "Input PIN"