from configparser import ConfigParser

config=ConfigParser()
config.read("C:\\Users\\KITS\\PycharmProjects\\ecommerceproject\\Configurations\\config.ini")

print(config.get('common info','baseURL'))




class Readconfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get('common info','baseURL')
        return url
    @staticmethod
    def getUsermail():
        un=config.get('common info','username')
        return un
    @staticmethod
    def getpassword():
        pw=config.get('common info','password')
        return pw
