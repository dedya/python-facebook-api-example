import configparser
import hashlib
import hmac

#from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

#read config.ini
config=configparser.ConfigParser()
folderPath = "D:/home/dedy/training/python-training/fb"
config.read(folderPath+'/config.ini')

def getFBConfig(param):
    return _getConfig('facebook',param)

def _getConfig(section,param):
    return config[section][param]

#generate fb appsecret_proof hash
def genAppSecretProof(app_secret, access_token):
    h = hmac.new (
        app_secret.encode('utf-8'),
        msg=access_token.encode('utf-8'),
        digestmod=hashlib.sha256
    )
    return h.hexdigest()
