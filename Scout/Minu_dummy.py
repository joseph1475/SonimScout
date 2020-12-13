from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


desired_caps1 = {
        "automationName": "UiAutomator2",  # Appium (default), or UiAutomator2
        "platformName": "Android",         # Andriod,IOS
        "platformVersion": "",             # can be open type or can declare the version .Eg: 8.1.1
        "deviceName": "903890ef",          # Android Emulator or 903e900a device ID
        "appPackage":  "com.sonim.scout",
        "appActivity" : "com.sonim.scout.activities.MainActivity"
    }

driver1 = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps1)
driver1.implicitly_wait(30)
wait = WebDriverWait(driver1, 5)
driver1.find_element_by_xpath("//android.widget.TextView[@text='SafeGuard']").click()
driver1.find_element_by_class_name("android.widget.Switch").click()
driver1.find_element_by_class_name("android.widget.EditText").send_keys(1234)
driver1.find_element_by_id("android:id/button1").click()
driver1.find_element_by_xpath("//*[@text='Applications']").click()
driver1.find_element_by_class_name("android.widget.EditText").send_keys(1234)
driver1.find_element_by_id("android:id/button1").click()
#SonimRestrictedAppsList = len(driver1.find_elements_by_id("com.sonim.safeguard:id/app_name"))
'''driver1.find_element_by_android_uiautomator("new UiScrollable(new UiSelector()."
            "resourceId(\"android:id/list\"))."com.sonim.safeguard:id/app_name
            "scrollIntoView(new UiSelector()."
            "textMatches(\"Zoom\")."
            "instance(0))")'''

# Find the list element.
list = driver1.find_element_by_id('com.sonim.safeguard:id/app_name')
# define touch
action = TouchAction(driver1)
SonimRestrictedAppsList = len(driver1.find_elements_by_id("com.sonim.safeguard:id/app_name"))
print(SonimRestrictedAppsList)
'''for i in range(SonimRestrictedAppsList):
    AppsName = (driver1.find_elements_by_id("com.sonim.safeguard:id/app_name")).__getitem__(i).text
    time.sleep(1)
    print(AppsName)'''
count = 0
# adjust here to your needs !
'''for x in range(0,4):
    wait.until(expected_conditions.presence_of_all_elements_located((By.ID, "com.sonim.safeguard:id/app_name")))
    SonimRestrictedAppsList = len(driver1.find_elements_by_id("com.sonim.safeguard:id/app_name"))
    count = count + SonimRestrictedAppsList
    for i in range(SonimRestrictedAppsList):
        AppsName = (driver1.find_elements_by_id("com.sonim.safeguard:id/app_name")).__getitem__(i).text
        time.sleep(1)
        print(AppsName)
    action.press(x=750, y=1750).move_to(x=0, y=-75).perform()
print(count)'''
'''restricting apps
size = driver1.find_element_by_id('android:id/list').size
print(size)
driver1.find_element_by_android_uiautomator(
    "new UiScrollable(new UiSelector()."
    "resourceId(\"android:id/list\"))."
    "scrollIntoView(new UiSelector()."
    "textMatches(\"Contacts\")."
    "instance(0))")
time.sleep(5)
driver1.find_element_by_xpath("//*[@text='Contacts']").click()
driver1.find_element_by_android_uiautomator(
    "new UiScrollable(new UiSelector()."
    "resourceId(\"android:id/list\"))."
    "scrollIntoView(new UiSelector()."
    "textMatches(\"WhatsApp\")."
    "instance(0))")
time.sleep(5)
driver1.find_element_by_xpath("//*[@text='WhatsApp']").click()
driver1.find_element_by_xpath("//*[@text='SAVE']").click()
driver1.press_keycode(4)
#appium_driver.driver.press_keycode4

desired_capsContacts = {
        "automationName": "UiAutomator2",  # Appium (default), or UiAutomator2
        "platformName": "Android",         # Andriod,IOS
        "platformVersion": "",             # can be open type or can declare the version .Eg: 8.1.1
        "deviceName": "903890ef",          # Android Emulator or 903e900a device ID
        "appPackage":  "com.android.contacts",
        "appActivity": "com.android.contacts.activities.PeopleActivity"
    }
Contactsdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capsContacts)
Contactsdriver.find_element_by_id("com.sonim.safeguard:id/editText").send_keys(1234)
desired_capsWhatsapp = {
        "automationName": "UiAutomator2",  # Appium (default), or UiAutomator2
        "platformName": "Android",         # Andriod,IOS
        "platformVersion": "",             # can be open type or can declare the version .Eg: 8.1.1
        "deviceName": "903890ef",          # Android Emulator or 903e900a device ID
        "appPackage":  "com.whatsapp",
        "appActivity": "com.whatsapp.HomeActivity"
    }
Whatsappdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capsWhatsapp)
Whatsappdriver.find_element_by_id("com.sonim.safeguard:id/editText").send_keys(1234)'''

'''cancel option
driver1.find_element_by_android_uiautomator(
    "new UiScrollable(new UiSelector()."
    "resourceId(\"android:id/list\"))."
    "scrollIntoView(new UiSelector()."
    "textMatches(\"Contacts\")."
    "instance(0))")
time.sleep(5)
driver1.find_element_by_xpath("//*[@text='Contacts']").click()
driver1.find_element_by_android_uiautomator(
    "new UiScrollable(new UiSelector()."
    "resourceId(\"android:id/list\"))."
    "scrollIntoView(new UiSelector()."
    "textMatches(\"WhatsApp\")."
    "instance(0))")
time.sleep(5)
driver1.find_element_by_xpath("//*[@text='WhatsApp']").click()
driver1.find_element_by_xpath("//*[@text='CANCEL']").click()
driver1.press_keycode(4)
#appium_driver.driver.press_keycode4

desired_capsContacts = {
        "automationName": "UiAutomator2",  # Appium (default), or UiAutomator2
        "platformName": "Android",         # Andriod,IOS
        "platformVersion": "",             # can be open type or can declare the version .Eg: 8.1.1
        "deviceName": "903890ef",          # Android Emulator or 903e900a device ID
        "appPackage":  "com.android.contacts",
        "appActivity": "com.android.contacts.activities.PeopleActivity"
    }
Contactsdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capsContacts)
contacts_title = driver1.find_element_by_xpath("//*[@text ='Contacts']").text
assert contacts_title == "Contacts"
desired_capsWhatsapp = {
        "automationName": "UiAutomator2",  # Appium (default), or UiAutomator2
        "platformName": "Android",         # Andriod,IOS
        "platformVersion": "",             # can be open type or can declare the version .Eg: 8.1.1
        "deviceName": "903890ef",          # Android Emulator or 903e900a device ID
        "appPackage":  "com.whatsapp",
        "appActivity": "com.whatsapp.HomeActivity"
    }
Whatsappdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capsWhatsapp)
whatsapp_title = driver1.find_element_by_xpath("//*[@text ='WhatsApp']").text
assert whatsapp_title == "WhatsApp"'''


'''select/unselect
driver1.find_element_by_xpath("//android.widget.ImageButton[contains(@index, '2')]").click()
driver1.find_element_by_xpath("//*[@text ='Select All']").click()
#count = 0
# adjust here to your needs !
for x in range(0,4):
    wait.until(expected_conditions.presence_of_all_elements_located((By.ID, "com.sonim.safeguard:id/app_name")))
    SonimRestrictedAppsList = len(driver1.find_elements_by_id("com.sonim.safeguard:id/app_name"))
    count = count + SonimRestrictedAppsList
    for i in range(SonimRestrictedAppsList):
        checkbox = driver1.find_element_by_android_uiautomator("new UiSelector().checked(true)")
        if checkbox == "false":
            count = count+1
            time.sleep(1)
    action.press(x=750, y=1750).move_to(x=0, y=-75).perform()
print(count)
driver1.find_element_by_xpath("//android.widget.ImageButton[contains(@index, '2')]").click()
driver1.find_element_by_xpath("//*[@text ='Unselect All']").click()
count2=0
for x in range(0,4):
    wait.until(expected_conditions.presence_of_all_elements_located((By.ID, "com.sonim.safeguard:id/app_name")))
    SonimRestrictedAppsList = len(driver1.find_elements_by_id("com.sonim.safeguard:id/app_name"))
    count = count + SonimRestrictedAppsList
    for i in range(SonimRestrictedAppsList):
        checkbox = driver1.find_element_by_android_uiautomator("new UiSelector().checked(false)")
        if checkbox == "false":
            count2 = count2+1
            time.sleep(1)
    action.press(x=750, y=1750).move_to(x=0, y=-75).perform()
print(count2)'''


'''search app
driver1.find_element_by_xpath("//*[@text ='Search applications']").send_keys("Photos")
photosApp =driver1.find_element_by_xpath("//*[@text ='Photos']").text
if photosApp == "Photos":
    print("success")'''


driver1.find_element_by_android_uiautomator(
    "new UiScrollable(new UiSelector()."
    "resourceId(\"android:id/list\"))."
    "scrollIntoView(new UiSelector()."
    "textMatches(\"Contacts\")."
    "instance(0))")
time.sleep(5)
driver1.find_element_by_xpath("//*[@text='Contacts']").click()
driver1.find_element_by_android_uiautomator(
    "new UiScrollable(new UiSelector()."
    "resourceId(\"android:id/list\"))."
    "scrollIntoView(new UiSelector()."
    "textMatches(\"WhatsApp\")."
    "instance(0))")
time.sleep(5)
driver1.find_element_by_xpath("//*[@text='WhatsApp']").click()
driver1.press_keycode(4)
discardMsg = driver1.find_element_by_id('android:id/message').text
if discardMsg == "Do you really want to discard these changes?":
    print("popup displayed")
    driver1.find_element_by_xpath("//*[@text = 'OK']").click()

activation =driver1.find_element_by_xpath("//*[@text = 'Activation']").text
print(activation)




''' wrong pin
driver1.find_element_by_xpath("//android.widget.TextView[@text='SafeGuard']").click()
driver1.find_element_by_class_name("android.widget.Switch").click()
driver1.find_element_by_class_name("android.widget.EditText").send_keys(4321)
driver1.find_element_by_xpath("//*[@text ='Enter PIN here']").clck()
driver1.find_element_by_xpath("//*[@text ='Wrong PIN']").text '''

