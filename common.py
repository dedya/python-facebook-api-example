import configparser
import hashlib
import hmac

#read config.ini
config=configparser.ConfigParser()
folderPath = "{path}"
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
