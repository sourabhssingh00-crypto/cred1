
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser): # special name, same you have to use # parser --> to add customer argument
    parser.addoption("--browser") # add a new command line option called --browser
    # Here have we just define the "--browser" not assigned any value to it.


@pytest.fixture(scope="class") # decorator
def browser_setup(request): # function
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("\nOpening chrome browser")
        #driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        # Create an "options" object for Chrome.
        # We use it to control Chrome settings before the browser launches.

        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            # This turns OFF Chrome's "credentials service"
            # Chrome will not offer to save usernames/passwords.
            "profile.password_manager_enabled": False
            # This turns OFF Chrome's built-in Password Manager feature.
            # Password Manager related popups (Save password / breach warning) will not come.
        }
                                               )
        driver = webdriver.Chrome(options=chrome_options)
        # Launch Chrome using the above options.
        # So Chrome starts with password manager disabled and those popups are avoided.


    elif browser == "firefox":
        print("\nOpening firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("\nOpening edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("\nOpening chrome headless browser")
        chrome_options = webdriver.ChromeOptions() #changing to firefox
        # FirefoxOptions = webdriver.FirefoxOptions()
        chrome_options.add_argument("--headless")
        # FirefoxOptions.add_argument("--headless")
        driver = webdriver.Chrome(options = chrome_options)
        # driver = webdriver.Chrome(options=FirefoxOptions)
    else:
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("prefs",{
             "credentials_enable_service": False,
             "profile.password_manager_enabled": False
        }
                                                  )
        print("\nOpening Firefox browser")
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver #new we are ataching the driver to main class
    yield driver
    print("\nBrowser Closed")
    driver.quit()

# Your task
# How to handle not secure site (certificate)
# Incognito/ Private window
# Password save browser message --> done
# Browser handle thr Remote desktop

#Test Data
# @pytest.fixture(params = [
#     ("Credencetest@test.com", "Credence@123", "login_pass"), # All correct #
#     ("Credencetest@test.com11", "Credence@123", "login_fail"), # username wrong #
#     ("Credencetest@test.com", "Credence@1231", "login_fail"), # password wrong
#     ("Credencetest@test.com1", "Credence@1231", "login_fail")  # username and password wrong
#
# ])
# def credkart_login_data(request):
#     return request.param


def pytest_metadata(metadata):
    metadata["Project Name"] = "Credkart Automation"
    metadata["Platform"] = "QA Platform"
    metadata["Tester Name"] = "Credence"
    metadata["Summary"] = " All test have executed"
    del metadata ["Platform"]