import pytest
from selenium import webdriver
import sys
sys.path.append("C:\\Users\\user\\PycharmProjects\\pythonProject_WE_MARCH")
print(sys.path)
from hybrid_framework.Utilities.ReadConfig import ReadProperty

@pytest.fixture()
def launch_browser(request):
    browser = request.config.getoption("--browser")
    if browser=="chrome":
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser=="edge":
        from selenium.webdriver.edge.service import Service
        service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif browser=="firefox":
        from selenium.webdriver.firefox.service import Service
        service_obj = Service(r"E:\selenium\drivers\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.get(ReadProperty.GetBaseURL())
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# cli hook
def pytest_addoption(parser):  # this will get the values from CLI/hooks
    parser.addoption("--browser")

