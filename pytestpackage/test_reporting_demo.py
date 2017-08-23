import pytest
from pytestpackage.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestReportingDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        result=self.abc.sumNumbers(2,8)
        assert result > 20
        print("Running method B")

#To generate report in html, type in terminal "pytest -s -v pytest/test_reporting_demo.py --browser firefox --html=htmlreport.html"

