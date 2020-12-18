import time

from appium import webdriver
from utilities.BaseClass import BaseClass
'''some contacts should be present in the device'''


class TestRestrictContacts(BaseClass):

    def test_addcontact(self):
        self.driver1.find_element_by_xpath("//android.widget.TextView[@text='SafeGuard']").click()
        self.driver1.find_element_by_xpath("//*[@text='Features']").click()
        self.driver1.find_element_by_class_name("android.widget.EditText").send_keys(1234)
        self.driver1.find_element_by_id("android:id/button1").click()
        self.driver1.find_element_by_android_uiautomator(
            "new UiSelector().textContains(\"Modify Contacts\")").click()
        self.driver1.find_element_by_xpath("//*[@text='SAVE']").click()
        desired_capsContacts = {
            "automationName": "UiAutomator2",  # Appium (default), or UiAutomator2
            "platformName": "Android",  # Andriod,IOS
            "platformVersion": "",  # can be open type or can declare the version .Eg: 8.1.1
            "deviceName": "903890ef",  # Android Emulator or 903e900a device ID
            "appPackage": "com.android.contacts",
            "appActivity": "com.android.contacts.activities.PeopleActivity"
        }
        Contactsdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capsContacts)
        Contactsdriver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()."
            "scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\"" + "Contacts" + "\").instance(0))");
        Contactsdriver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
        '''popup = Contactsdriver.find_element_by_id("com.android.contacts:id/text").text
        if popup == "Choose a default account for new contacts:":
            Contactsdriver.find_element_by_xpath("//*[@text='PHONE']").click()
            enterpin = Contactsdriver.find_element_by_xpath("//*[@text='Enter PIN']").text
            assert enterpin == "Enter PIN"
        else:
            enterpin = Contactsdriver.find_element_by_xpath("//*[@text='Enter PIN']").text
            assert enterpin == "Enter PIN"'''
        title = Contactsdriver.find_element_by_id("android:id/action_bar_title").text
        assert title == "SafeGuard"
        Contactsdriver.press_keycode(4)

    def test_editcontact(self):
        desired_capsContacts = {
            "automationName": "UiAutomator2",  # Appium (default), or UiAutomator2
            "platformName": "Android",  # Andriod,IOS
            "platformVersion": "",  # can be open type or can declare the version .Eg: 8.1.1
            "deviceName": "903890ef",  # Android Emulator or 903e900a device ID
            "appPackage": "com.android.contacts",
            "appActivity": "com.android.contacts.activities.PeopleActivity"
        }
        Contactsdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capsContacts)
        Contactsdriver.find_element_by_xpath("//android.view.ViewGroup[contains(@index, '1')]").click()
        Contactsdriver.find_element_by_xpath("//android.widget.TextView[contains(@index, '1')]").click()
        time.sleep(2)
        title = Contactsdriver.find_element_by_id("android:id/action_bar_title").text
        assert title == "SafeGuard"
        Contactsdriver.press_keycode(4)

    def test_deleteContact(self):
        desired_capsContacts = {
            "automationName": "UiAutomator2",  # Appium (default), or UiAutomator2
            "platformName": "Android",  # Andriod,IOS
            "platformVersion": "",  # can be open type or can declare the version .Eg: 8.1.1
            "deviceName": "903890ef",  # Android Emulator or 903e900a device ID
            "appPackage": "com.android.contacts",
            "appActivity": "com.android.contacts.activities.PeopleActivity"
        }
        Contactsdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capsContacts)
        Contactsdriver.find_element_by_xpath("//android.view.ViewGroup[contains(@index, '1')]").click()
        Contactsdriver.find_element_by_xpath("//android.widget.ImageButton[contains(@index, '2')]").click()
        time.sleep(2)
        Contactsdriver.find_element_by_xpath("//android.widget.TextView[@text='Delete']").click()
        title = Contactsdriver.find_element_by_xpath("//android.widget.TextView[contains(@index, '0')]").text
        assert title == "SafeGuard"
        Contactsdriver.press_keycode(4)
