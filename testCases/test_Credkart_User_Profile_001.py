"""
Testcases:
login
registration
checkout
amount verification
logout with params
login with Excel
registration with params
registration with Excel

"""
import allure
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class
from utilities.Logger import log_generator_class
from utilities.readConfig import ReadConfigClass


@pytest.mark.usefixtures("browser_setup")#new
class Test_User_Profile:
    driver = None
    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    login_url = ReadConfigClass.get_data_for_login_url()
    registration_url = ReadConfigClass.get_data_for_registration_url()
    log = log_generator_class.log_gen_method()



    @allure.title("test_verify_Credkart_url_001")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.epic("Epic: Userprofile")
    @allure.description("This testcases is to validate CredKart website title")
    @allure.link(login_url)
    @allure.issue("title verification")
    @allure.story("CredKart : User login")
    @pytest.mark.smoke
    # @pytest.mark.flaky(reruns=1, rerun_delay=1)
    @pytest.mark.dependency(name = "test_verify_Credkart_url_001")
    @pytest.mark.order(1)
    def test_verify_Credkart_url_001(self):
        # self.log.debug("this is a debug message")
        # self.log.info("this is info")
        # self.log.warning("this is a warning")
        # self.log.error("this ia error")
        # self.log.critical("this is a critical")

        self.log.info("Testcase test_verify_Credkart_url_001 is started")
        self.driver.get(self.login_url)
        self.log.info(f"opening browser and getting {self.login_url}")
        self.log.info(f"checking driver title")
        if self.driver.title == "CredKart":
            print(f"driver.title-->{self.driver.title}")
            self.log.info(f"Testcase test_verify_Credkart_url_001 is passed")
            self.log.info(f"Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_Credkart_User_Profile_001_pass.png")
            allure.attach.file(".\\Screenshots\\test_Credkart_User_Profile_001_pass.png",
                               attachment_type=allure.attachment_type.PNG)
        else:
            self.log.info(f"Testcase test_verify_Credkart_url_001 is failed")
            self.log.info(f"Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_Credkart_User_Profile_001_fail.png")
            allure.attach.file(".\\Screenshots\\test_Credkart_User_Profile_001_fail.png",
                               attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info(f"Testcase test_verify_Credkart_url_001 is completed")



    @allure.title("test_Credkart_login_002")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic("Epic: Userprofile: user login")
    @allure.description("This testcases is to validate CredKart website  user login")
    @allure.link(login_url)
    @allure.issue("user login")
    @allure.story("CredKart : User login")
    # @pytest.mark.smoke
    # @pytest.mark.flaky(reruns=1, rerun_delay=1)
    #@pytest.mark.dependency(depends=["test_verify_Credkart_url_001"])
    @pytest.mark.order(2)
    def test_Credkart_Login_002(self):

        self.log.info(f"Testcase test_verify_Credkart_url_002 is starting")
        self.driver.get(self.login_url)
        self.log.info(f"Opening browser and getting {self.login_url}")

        # email_id = "Credencetest@test.com"
        # pass_word = "Credence@123"
        from pageObjects.Login_Page import Login_Page_Class
        self.lp = Login_Page_Class(self.driver)

        # Enter Username
        self.log.info(f"Entering the email--> {self.email}")
        self.lp.Enter_Email(self.email)

            # Enter Password
        self.log.info(f"Entering the password")
        self.lp.Enter_password(self.password)

            # Click on Login button
        self.log.info(f"clicking the login button")
        self.lp.Click_Login_Button()



        # try:
        #
        #     element = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
        #     print("User Login Successful")
        #     self.driver.save_screenshot(f"User Login Successful_{email_id}.png")
        #     menu = self.driver.find_element(By.XPATH, "//a[@role='button']")
        #     menu.click()
        #     logout = self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        #     logout.click()
        #
        # except:
        #     print("User Login Fail")
        #     self.driver.save_screenshot(f"User Login Fail_{email_id}.png")
        #     assert False, "User Login Fail"

        self.log.info(f"checking the login status")
        if self.lp.verify_menu_button_visibility() == "pass":
            self.log.info(f"User Login successful and taking screenshot")
            self.driver.save_screenshot(f"User Login Successful_{self.email}.png")
            allure.attach.file(f".\\Screenshots\\User Login Successful_{self.email}",
                               attachment_type=allure.attachment_type)
            self.log.info(f"clicking menu button")
            self.lp.Click_menu_button()
            self.log.info(f"clicking the logout button")
            self.lp.Click_Logout_Button()
        else:
            self.log.info(f"User Login fail and taking screenshot")
            self.driver.save_screenshot(f"User Login Successful_{self.email}.png")
            allure.attach.file(f".\\Screenshots\\User Login Fail_{self.email}",
                               attachment_type=allure.attachment_type.PNG)
            assert False, "User Login Fail"
        self.log.info(f"Testcase test_verify_Credkart_url_002 is completed")



    @allure.title("test_Credkart_registration_003")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.epic("Epic: Userprofile: user registration")
    @allure.description("This testcases is to validate CredKart website user registration")
    @allure.link(login_url)
    @allure.issue("user registration")
    @allure.story("CredKart : User registration")
    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=1, rerun_delay=1)
    #@pytest.mark.dependency(depends=["test_verify_Credkart_url_001"])
    @pytest.mark.order(3)
    def test_Credkart_registration_003(self):
        self.log.info(f"Testcase test_verify_Credkart_url_003 is starting")

        self.driver.get(self.registration_url)
        self.log.info(f"Opening browser and getting {self.registration_url}")
        fake_email = ""
        fake_username = Faker().user_name()  # New
        fake_email = Faker().email()  # New
        self.log.info(f"Generated fake data for username --> {fake_username} and email --> {fake_email}")
        password_data = "Credence_user_101@123"



        self.rp = Registration_Page_Class(self.driver)

        # Enter Username
        self.rp.Enter_Name(fake_username)
        self.log.info(f"entering the username--> {fake_username}")
        # Enter Email
        self.rp.Enter_Email(fake_email)
        self.log.info(f"entering the email--> {fake_email}")
        # Enter Password
        self.rp.Enter_password(password_data)
        self.log.info(f"entering the password")
        # Enter Confirm Password
        self.rp.Enter_Confirm_Password(password_data)
        self.log.info(f"entering the confirm password")
        # Click on register button
        self.log.info(f"clicking the registration button")
        self.rp.Click_Login_Register_Button()

        if self.rp.verify_menu_button_visibility() == "pass":
            self.log.info(f"User registration successful and taking screenshot")
            self.driver.save_screenshot(f"User Registration Successful_{fake_username}.png")
            allure.attach.file(f".\\Screenshots\\User Registration Successful_{fake_username}.png",
                               attachment_type=allure.attachment_type.PNG)
            self.log.info(f"clicking menu button")
            self.rp.Click_menu_button()
            self.log.info(f"clicking on logout button")
            self.rp.Click_Logout_Button()
        else:
            self.log.info(f"User registration fail and taking screenshot")
            self.driver.save_screenshot(f"User Registration Fail_{fake_username}.png")
            allure.attach.file(f".\\Screenshots\\User Registration Fail_{fake_username}.png",
                               attachment_type=allure.attachment_type.PNG)
            assert False, "User Registration Fail"
        self.log.info(f"Testcase test_verify_Credkart_url_003 is completed")




# pytest -v -s -n=auto --html=Html_reports\my_reports.html
# pytest -v -s -n=auto --html=Html_reports\my_reports.html --browser headless
# pytest --alluredir="AllureReports" -n=auto --browser headless
# allure serve "AllureReports"