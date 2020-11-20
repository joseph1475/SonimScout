import pytest
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction


@pytest.fixture(scope="class")
def setup(request):
    desired_caps1 = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        "platformVersion": "",
        "deviceName": "67a9c223",
        "appPackage": "com.sonim.scout",
        "appActivity": "com.sonim.scout.activities.MainActivity"

    }

    driver1 = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
    driver1.implicitly_wait(30)
    request.cls.driver1 = driver1

    yield
    print("\n", "End")
    driver1.quit()
