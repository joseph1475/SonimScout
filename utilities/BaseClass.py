import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self,elementtext):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, elementtext)))

    def CorrectPIN(self):
        self.driver1.find_element_by_id("com.sonim.safeguard:id/dialog_edit_text").send_keys(1234)
        self.driver1.hide_keyboard()
        self.driver1.find_element_by_class_name("android.widget.Button").click()

    def SafeGuardActivation(self):
        self.driver1.find_element_by_id("com.sonim.safeguard:id/switch_bar").click()

    def SafeGuardDisabling(self):
        self.driver1.find_element_by_id("com.sonim.safeguard:id/switch_bar").click()




