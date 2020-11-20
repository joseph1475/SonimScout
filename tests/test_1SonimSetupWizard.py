import pytest

from PageObjects.SonimScoutSetup import SonimScoutSetup
from utilities.BaseClass import BaseClass


class TestScout(BaseClass):
    def test_SonimSetupWizard(self):
        Wizard = SonimScoutSetup(self.driver1)
        Wizard.ScoutSetup().click()

    def test_SonimSetupWizardHeading(self):
        Wizard.Quit().click()

        #self.driver.find_element_by_xpath("//*[@text='Sonim Setup Wizard']").click()
        #self.driver.find_element_by_id("com.sonimtech.setupwizard.ten:id/btnQuit").click()
