import time
from utilities.BaseClass import BaseClass


class Test_SONIM_SetupWizard(BaseClass):
    # PageTitle
    def test_PageTitle(self):
        # launch Sonim Setuo Wizard
        self.driver1.find_element_by_xpath("//*[@text='Sonim Setup Wizard']").click()
        PageTitle = self.driver1.find_element_by_id(
            "com.sonimtech.setupwizard.ten:id/action_bar").find_element_by_xpath(
            "//*[@class='android.widget.TextView']").text
        print(PageTitle)
        time.sleep(2)

    # txtViewInformation
    def test_txtViewInformation(self):
        txtViewInformation = self.driver1.find_element_by_id("com.sonimtech.setupwizard.ten:id/txtViewInformation").text
        print(txtViewInformation)
        time.sleep(2)

    # SCAN button
    def test_SCANbutton(self):
        self.driver1.find_element_by_id("com.sonimtech.setupwizard.ten:id/btnScan").click()
        self.driver1.keyevent(4)
        time.sleep(2)

    # HOME button
    def test_HOMEbutton(self):
        self.driver1.find_element_by_id("com.sonimtech.setupwizard.ten:id/btnQuit").click()
