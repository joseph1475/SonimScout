'''
Sonim SafeGuard Main Screen UI
"Following menu SHALL be provided in the Sonim SafeGuard Application (sub-text)
1) Activation
2) Applications (Restrict Apps)
3) Features (Restrict Features)
4) Change PIN (Change your PIN)
5) Application PIN Timeout (Change PIN time out)"
"About" should be available via overflow menu
"Help" should be available via overflow menu
'''
import pytest
import time
from utilities.BaseClass import BaseClass

class TestSonimSafeGuardMainScreenUI(BaseClass):
    def test_SafeGuardApplicationLaunch(self):
        self.driver1.find_element_by_xpath("//*[@text='SafeGuard']").click()

    def test_ItemsInMainScreenUItitles(self):
        print("Following menu Titles SHALL be provided in the Sonim SafeGuard Application ")
        switch_text = self.driver1.find_element_by_id("com.sonim.safeguard:id/switch_text")
        print("==============================")
        print(switch_text.text)
        assert switch_text.text == "Activation"
        SonimSafeGuardMainScreenUI = len(self.driver1.find_elements_by_id("android:id/title"))
        for i in range(SonimSafeGuardMainScreenUI):
            Titles = (self.driver1.find_elements_by_id("android:id/title")).__getitem__(i).text
            print("==============================")
            print("Title:" + Titles)

            if Titles == "Applications":
                Subtext = len(self.driver1.find_elements_by_id("android:id/summary"))
                for j in range(Subtext):
                    text = (self.driver1.find_elements_by_id("android:id/summary")).__getitem__(0).text
                    print(text)
                    assert text == "Restrict Apps"
                    break

            if Titles == "Features":
                Subtext = len(self.driver1.find_elements_by_id("android:id/summary"))
                for j in range(Subtext):
                    text = (self.driver1.find_elements_by_id("android:id/summary")).__getitem__(1).text
                    print(text)
                    assert text == "Restrict Features"
                    break

            if Titles == "Change PIN":
                Subtext = len(self.driver1.find_elements_by_id("android:id/summary"))
                for j in range(Subtext):
                    text = (self.driver1.find_elements_by_id("android:id/summary")).__getitem__(2).text
                    print(text)
                    assert text == "Change your PIN"
                    break

            if Titles == "Application PIN Timeout":
                Subtext = len(self.driver1.find_elements_by_id("android:id/summary"))
                for j in range(Subtext):
                    text = (self.driver1.find_elements_by_id("android:id/summary")).__getitem__(3).text
                    print(text)
                    assert text == "Change PIN time out"
                    break

            if Titles == "Version":
                Subtext = len(self.driver1.find_elements_by_id("android:id/summary"))
                for j in range(Subtext):
                    text = (self.driver1.find_elements_by_id("android:id/summary")).__getitem__(4).text
                    print(text)
                    break
