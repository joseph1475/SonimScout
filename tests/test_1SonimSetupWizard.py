import pytest

from PageObjects.SonimScoutSetup import SonimScoutSetup
from utilities.BaseClass import BaseClass


class TestScout(BaseClass):
    def test_SonimSetupWizard(self):
        Wizard = SonimScoutSetup(self.driver1)
        SetupWizardString = Wizard.ScoutSetup().text
        print(SetupWizardString)
        assert SetupWizardString == "Sonim Setup Wizard", "String mismatch"

    def test_SonimSetupWizardPageHeading(self):
        Wizard = SonimScoutSetup(self.driver1)
        if SetupWizardString == "Sonim Setup Wizard":
            Wizard.ScoutSetup().click()
            self.verifyElementPresence("//android.widget.TextView[@text='SonimSetupWizard']")
            WizardHeading = Wizard.find_element_by_xpath("//android.widget.TextView[@text='SonimSetupWizard']").text
            assert WizardHeading == "Sonim Setup Wizard", "String Mismatch"

    def test_SonimSetupWizardScan(self):
        Wizard = SonimScoutSetup(self.driver1)
        # Wizard.find_element_by_id("com.sonimtech.setupwizard.ten:id/btnScan").click()
        # self.verifyElementPresence("//android.widget.Button[@text='SCAN']")
        Wizard.find_element_by_xpath("//android.widget.Button[@text='SCAN']").text
        Wizard.find_element_by_xpath("//android.widget.Button[@text='SCAN']").click()
        Wizard.Quit().click()


        #self.driver.find_element_by_xpath("//*[@text='Sonim Setup Wizard']").click()
        #self.driver.find_element_by_id("com.sonimtech.setupwizard.ten:id/btnQuit").click()
