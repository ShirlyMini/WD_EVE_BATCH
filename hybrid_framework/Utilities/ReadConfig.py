import configparser

ini_data = configparser.RawConfigParser()
ini_data.read(r"C:\Users\user\PycharmProjects\pythonProject_WE_MARCH\hybrid_framework\Configurations\config.ini")
#example
# print(ini_data.get("common data", "url"))

class ReadProperty:
    @staticmethod
    def GetBaseURL():
        return ini_data.get("common data", "url")

    @staticmethod
    def GetUserName():
        return ini_data.get("common data", "user")

    @staticmethod
    def GetPassword():
        return ini_data.get("common data", "password")