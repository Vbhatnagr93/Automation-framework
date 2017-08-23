import unittest

class TestCaseDemo(unittest.TestCase): #We need to inherit Testcase class from unittest

    def setUp(self):
        #We call the setUp before each test method
        print("I will run once before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")


    def tearDown(self):
        #tearDown cleans up any initialized values after test is executed. It is optional
        print("I will run after every test")

if __name__ =='__main__':
    unittest.main(verbosity=2)



