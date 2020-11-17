'''
from appium import webdriver
import time

desired_caps1 = {
        "automationName": "UiAutomator2",  # Appium (default), or UiAutomator2
        "platformName": "Android",         # Andriod,IOS
        "platformVersion": "",             # can be open type or can declare the version .Eg: 8.1.1
        "deviceName": "903e900a",          # Android Emulator or 903e900a device ID
        "appPackage":  "com.sonim.scout",
        "appActivity" : "com.sonim.scout.activities.MainActivity"
    }

driver1 = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps1)
driver1.implicitly_wait(30)
driver1.find_element_by_xpath("//*[@text='SafeGuard']").click() #SafeGuard launch
driver1.find_element_by_id("com.sonim.safeguard:id/switch_bar").click()#Activation
#Input PIN
driver1.find_element_by_id("com.sonim.safeguard:id/dialog_edit_text").send_keys(1234)
driver1.hide_keyboard()
driver1.find_element_by_class_name("android.widget.Button").click()

#Restrict Applications SHALL allow the User to configure list of applications that SHOULD be guarded by Sonim SafeGuard
#All the applications installed or pre-installed in the device SHALL be allowed to be safe guarded
#On selecting "Applications" menu, Sonim SafeGuard SHALL prompt the User for a PIN
driver1.find_element_by_xpath("//*[@text='Applications']").click()
InputPIN = driver1.find_element_by_xpath("//*[@text = 'Enter PIN here']").text
assert InputPIN == 'Enter PIN here'
#"On successful PIN verification application SHALL display alphabetical list of launchable applications on the phone with a check box for each item to enable/disable the application"
driver1.find_element_by_id("com.sonim.safeguard:id/dialog_edit_text").send_keys(1234)
driver1.hide_keyboard()
driver1.find_element_by_class_name("android.widget.Button").click()




#Save and Cancel option SHALL be provided in the list screen to save/cancel the current operation
option1 = driver1.find_element_by_id("com.sonim.safeguard:id/action_save").text
option2 = driver1.find_element_by_id("com.sonim.safeguard:id/action_cancel").text
print(option1,option2)
assert option1 == "SAVE"
assert option2 == "CANCEL"
#Save and Cancel option SHALL be provided in the overflow menu
#On selecting Save option User operation SHALL be saved and SHALL navigate to previous screen
#On selecting Cancel option User operation SHALL be cancelled and SHALL navigate to previous screen
driver1.find_element_by_id("com.sonim.safeguard:id/action_cancel").click()
#On PIN verification failure, Sonim SafeGuard SHALL display a relevant message to the User
driver1.find_element_by_xpath("//*[@text='Applications']").click()
driver1.find_element_by_id("com.sonim.safeguard:id/dialog_edit_text").send_keys(12345)
driver1.hide_keyboard()
driver1.find_element_by_class_name("android.widget.Button").click()
driver1.find_element_by_id("com.sonim.safeguard:id/dialog_edit_text").click()
time.sleep(2)
driver1.keyevent(4)
time.sleep(2)
#alertPopup = driver1.switch_to.alert
#time.sleep(2)
#PopupMessage = alertPopup.text
PopupMessage = driver1.find_element_by_id("com.sonim.safeguard:id/dialog_edit_text").text
print(PopupMessage)
if PopupMessage == "Enter PIN here":
        print("Wrong PIN")
else:
        print("Correct password")
#Restrict Applications screen SHALL display the application list with current state of the restriction
#Restrict Applications screen SHALL  have “Select all/Unselect all” option to select/unselect all the applications at once in overflow menu.
#Restrict Applications option SHALL be greyed out when the Activation is set to OFF and should only be accessible when Activation is set to ON
#Restrict Application SHALL have a timeout setting. This timeout SHALL define the time interval during which the PIN screen will not be prompted for the application
#Restrict Applications screen SHALL have "Search" option to search a particular application. Search SHALL be case insensitive.
#Restriction Applications screen "Search" option should default to alphanumeric keyboard when selected
#If User makes a change to Restrict Applications list and tries to navigate away from the Restrict Applications screen without saving, they should be presented with a dialog box -> "Discard Changes" -> "Do you really want to discard these changes?" -> Options to "Cancel" (return to Apps list) and "OK" (follow Android behavior of navigation)


'''


# Python3 program to print
# all repeating elements
def printRepeating(arr, n):
        # Store elements and
        # their counts in
        # hash table
        mp = [0] * 100
        for i in range(0, n):
                mp[arr[i]] += 1

        # Since we want elements
        # in same order, we
        # traverse array again
        # and print those elements
        # that appear more than once.
        for i in range(0, n):
                if (mp[arr[i]] > 1):
                        print(arr[i], end=" ")

                        # This is tricky, this
                        # is done to make sure
                        # that the current element
                        # is not printed again
                        mp[arr[i]] = 0


# Driver code
arr = [12, 10, 9, 45,
       2, 10, 10, 45]
n = len(arr)
printRepeating(arr, n)






