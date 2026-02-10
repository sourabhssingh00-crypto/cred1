
import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
# config.read(".\\..\\Configurations\\config.ini")
# config.read("C:\Users\Sourabh\Desktop\retest\Configurations\config.ini")

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

#
# import configparser
# import os
#
# config = configparser.RawConfigParser()
#
# # This finds the directory of readConfig.py, then goes up to the project root
# current_dir = os.path.dirname(os.path.abspath(__file__))
# config_path = os.path.join(current_dir, "..", "Configurations", "config_SIT.ini")
#
# config.read(config_path)
#
#
# class ReadConfigClass:
#     @staticmethod
#     def get_data_for_email():
#         return config.get("login_data", "email")
#
#     @staticmethod
#     def get_data_for_password():
#         return config.get("login_data", "password")
#
#     # ... keep other methods as is ...



