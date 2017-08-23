import unittest

class TestCaseDemo(unittest.TestCase):

    @classmethod #Decorators in python
    def setUpClass(cls): #This is class level setup method
        print("*"*30)
        print("I will run only once before all tests")
        print("*" * 30)

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

    @classmethod
    def tearDownClass(cls): #This is class level teardown method
        print("*" * 30)
        print("I will run only once after all tests")
        print("*" * 30)


if __name__ =='__main__':
    unittest.main(verbosity=2)



