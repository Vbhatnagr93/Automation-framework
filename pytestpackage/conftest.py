import pytest

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.fixture( scope="class")
def oneTimeSetUp(request, browser, osType):

    print("Running one time setUp")
    if browser == 'firefox':
        value = 10
        print("Running Tests on FF")
    else:
        value = 20
        print("Running tests on Chrome")
    if request.cls is not None:
        request.cls.value = value

    yield value
    print("Running one time tearDown")


#To run our test cases in different environments
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


# To run in terminal, type "py.test path/test_conftest_demo*.py". If you are in the current directory, you can remove "path"

