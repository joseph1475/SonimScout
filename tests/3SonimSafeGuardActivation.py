import time
from appium import webdriver

from utilities.BaseClass import BaseClass


class Test_SonimSafeGuardActivation(BaseClass):
    '''
    Activation
    Activation option SHALL allow the User to enable/disable the Sonim SafeGuard feature
    Activation option SHALL be modified (enabled/ disabled) with a PIN input
            Actication option SHALL be a configuration which SHALL persist across device reboots
    By default, none of the applications/features SHALL be SafeGuarded. Admin SHALL configure the application/feature list after activation
    On selecting this feature, device SHALL prompt the User to enter the PIN code for verification
    If this feature is active and User tries to open any application that is SafeGuarded then User SHALL be prompted for PIN code verification.
    Sonim SafeGuard SHALL prompt the User for a PIN to access the application/feature that is safe guarded
    PIN code verification screen SHALL have Ok option menu
    On selecting Ok option of the PIN code screen, application SHALL verify the User entered PIN
    If PIN verification is successful, then User SHALL be allowed to activate / de-activate the Sonim SafeGuard feature.
    '''
    def test_SafeGuardApplicationActivation(self):
        self.driver1.find_element_by_xpath("//*[@text='SafeGuard']").click()
        print("Activation option SHALL allow the User to enable the Sonim SafeGuard feature")
        self.SafeGuardActivation()

    def test_SafeGuardDefaultPIN(self):
        print("Activation option SHALL be modified (enabled) with a PIN input")
        self.CorrectPIN()

    def test_SafeGuardlist(self):
        print("By default, none of the applications/features SHALL be SafeGuarded.")
        SonimSafeGuardMainScreenUI = len(self.driver1.find_elements_by_id("android:id/title"))
        for i in range(SonimSafeGuardMainScreenUI):
            Titles = (self.driver1.find_elements_by_id("android:id/title")).__getitem__(i).text
            print(Titles)
            if Titles == "Applications":
                self.driver1.find_elements_by_class_name("android.widget.RelativeLayout").__getitem__(i).click()
                break
        assert Titles == "Applications"
        # Input PIN
        self.driver1.find_element_by_id("com.sonim.safeguard:id/dialog_edit_text").send_keys(1234)
        self.driver1.hide_keyboard()
        self.driver1.find_element_by_class_name("android.widget.Button").click()

        self.driver1.find_element_by_class_name("android.widget.LinearLayout").find_element_by_class_name(
            "android.widget.ImageButton").click()
        self.driver1.find_element_by_id("android:id/title").click()

        self.driver1.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()."
            "resourceId(\"android:id/list\"))."
            "scrollIntoView(new UiSelector()."
            "textMatches(\"Zoom\")."
            "instance(0))")

        self.driver1.find_element_by_class_name("android.widget.LinearLayout").find_element_by_class_name(
            "android.widget.ImageButton").click()
        self.driver1.find_element_by_xpath("//*[@text='Unselect All']").click()


    def test_SelectAppName(self):

        print("Admin SHALL configure the application/feature list after activation")
        print("On selecting this feature, device SHALL prompt the User to enter the PIN code for verification")
        '''
        SonimSafeGuardMainScreenUI = len(self.driver1.find_elements_by_id("android:id/title"))
        for i in range(SonimSafeGuardMainScreenUI):
            Titles = (self.driver1.find_elements_by_id("android:id/title")).__getitem__(i).text
            if Titles == "Applications":
                self.driver1.find_elements_by_id("android:id/title").__getitem__(0).click()
                break
        self.CorrectPIN()
        '''
        # Scrolling to find application
        self.driver1.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()."
            "resourceId(\"android:id/list\"))."
            "scrollIntoView(new UiSelector()."
            "textMatches(\"Calculator\")."
            "instance(0))")
        time.sleep(5)
        self.driver1.find_element_by_xpath("//*[@text='Calculator']").click()
        self.driver1.find_element_by_id("com.sonim.safeguard:id/action_save").click()

    def test_LaunchCalculator(self):
        print("If this feature is active and User tries to open any application that is SafeGuarded then User SHALL be prompted for PIN code verification.")
        desired_caps2 = {
            "automationName": "UiAutomator2",
            "platformName": "Android",
            "platformVersion": "",
            "deviceName": "903e900a",
            "appPackage": "com.google.android.calculator",
            "appActivity": "com.android.calculator2.Calculator",
        }
        driver2 = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps2)
        driver2.implicitly_wait(30)
        driver2.find_element_by_id("com.sonim.safeguard:id/editText").click()
        print("Sonim SafeGuard SHALL prompt the User for a PIN to access the application/feature that is safe guarded")
        driver2.find_element_by_id("com.sonim.safeguard:id/editText").send_keys(1234)
        driver2.hide_keyboard()
        ok_button = driver2.find_element_by_id("com.sonim.safeguard:id/action_ok").text
        print("PIN code verification screen SHALL have Ok option menu")
        print("selected:" + ok_button)
        assert ok_button == "OK"
        driver2.find_element_by_id("com.sonim.safeguard:id/action_ok").click()
        driver2.press_keycode(4)
        time.sleep(2)

    def test_RelaunchSafeGuard(self):
        self.driver1.start_activity(app_package="com.sonim.scout",app_activity="com.sonim.scout.activities.MainActivity")
        self.driver1.find_element_by_xpath("//*[@text='SafeGuard']").click()

    def test_SafeGuardApplicationDisabling(self):
        print("On selecting Ok option of the PIN code screen, application SHALL verify the User entered PIN")
        print("Activation option SHALL allow the User to disable the Sonim SafeGuard feature")
        self.SafeGuardDisabling()

    def test_SafeGuardDisableWithPIN(self):
        print("Activation option SHALL be modified (disabled) with a PIN input")
        print("If PIN verification is successful, then User SHALL be allowed to activate / de-activate the Sonim SafeGuard feature.")
        self.CorrectPIN()