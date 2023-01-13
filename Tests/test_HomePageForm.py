import time

import pytest

from Page_obj.HomePageForm import HomePageFormObj
from utilities.BaseClass import Base


class Test_HomePageForm(Base):

    def test_HomePageForm(self, setData):

        HomePageFormdriver = HomePageFormObj(self.driver)
        log = self.test_loggingDemo()
        HomePageFormdriver.setName().send_keys(setData["firstname"])
        log.info("get all info")
        HomePageFormdriver.setEmail().send_keys(setData["mail"])
        HomePageFormdriver.setGender(setData["gender"])

        HomePageFormdriver.setSubmit().click()



        time.sleep(2)
        text = HomePageFormdriver.getSuccessText().text
        assert text == "×\nSuccess! The Form has been submitted successfully!."
        self.driver.refresh()




    @pytest.fixture(params=[{"firstname": "xyz", "mail": "xyz@mail.com", "gender": "Female"},
                            {"firstname": "xyz1", "mail": "xyz1@mail.com", "gender": "Female"}])
    def setData(self, request):
        return request.param
