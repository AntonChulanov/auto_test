import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru en fr")


@pytest.fixture(scope="function")
def language(request):
    language_name = request.config.getoption("language")
    return language_name


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    #language = None
   # if language_name == "es":
   #     print("\nes")
   #     language = "es"
   # elif language_name == "fr":
   #     print("\nfr")
   #     language ="fr"
    #else:
    #    raise pytest.UsageError("--browser_name should be chrome or firefox")
    #yield browser
    #print("\nquit browser..")
    
