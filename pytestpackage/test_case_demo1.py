import pytest

@pytest.fixture()
def setUp():
    print("Running demo1 setUp")

def test_demo1_methodA(setUp):
    print("Running demo1 method A")

def test_demo1_methodB(setUp):
    print("Running demo1 method B")

# To run in terminal, type "py.test -s test_case_demo1.py" or "py.test -s -v"
# Make sure to run from directory where file is saved
