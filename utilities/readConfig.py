
import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
# config.read(".\\..\\Configurations\\config.ini")

class ReadConfigClass:


    @staticmethod
    def get_data_for_email():
        return config.get("login_data", "email")

    @staticmethod
    def get_data_for_password():
        return config.get("login_data", "password")

    @staticmethod
    def get_data_for_login_url():
        return config.get("application_url", "login_url")

    @staticmethod
    def get_data_for_registration_url():
        return config.get("application_url", "registration_url")



