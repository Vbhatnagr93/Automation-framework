import pytest
@pytest.fixture()
def setUp():
    print("Running demo2 setUp") # More like SetUp method in unittest
    yield
    print("Running demo2 tearDown") # More like TearDown method in unittest

def test_demo2_methodA(setUp):
    print("Running demo2 method A")

def test_demo2_methodB(setUp):
    print("Running demo2 method B")