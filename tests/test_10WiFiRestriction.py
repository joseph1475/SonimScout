import time

from appium import webdriver
from utilities.BaseClass import BaseClass


class TestRestrictWiFi(BaseClass):

    def test_wifiSettings(self):
        self.driver1.find_element_by_xpath("//android.widget.TextView[@text='SafeGuard']").click()
        self.driver1.find_element_by_xpath("//*[@text='Features']").click()
        self.driver1.find_element_by_class_name("android.widget.EditText").send_keys(1234)
        self.driver1.find_element_by_id("android:id/button1").click()
        self.driver1.find_element_by_android_uiautomator(
            "new UiSelector().textContains(\"WiFi Restriction\")").click()
        self.driver1.find_element_by_xpath("//*[@text='SAVE']").click()
        desired_capsSettings = {
            "automationName": "UiAutomator2",  # Appium (default), or UiAutomator2
            "platformName": "Android",  # Andriod,IOS
            "platformVersion": "",  # can be open type or can declare the version .Eg: 8.1.1
            "deviceName": "903890ef",  # Android Emulator or 903e900a device ID
            "appPackage": "com.android.settings",
            "appActivity": "com.android.settings.Settings"
        }
        Settingsdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capsSettings)
        Settingsdriver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()."
            "scrollable(true).instance(0))."
            "scrollIntoView(new UiSelector().textContains(\"" + "Network & Internet" + "\").instance(0))");
        time.sleep(5)
        Settingsdriver.find_element_by_android_uiautomator(
            "new UiSelector().textContains(\"Network & Internet\")").click()
        Settingsdriver.find_element_by_xpath("//android.widget.Switch[@text='ON']").click()
        title = Settingsdriver.find_element_by_id("android:id/action_bar_title").text
        assert title == "SafeGuard"
