from common import genAppSecretProof,getFBConfig
import facebook
from datetime import datetime

def main():
    my_app_secret=getFBConfig('app_secret')
    my_access_token=getFBConfig('access_token')
    app_secret_proof = genAppSecretProof(my_app_secret,my_access_token)

    graph = facebook.GraphAPI(access_token=my_access_token)
    fields=['id','name','access_token']

    my_fields = ",".join(fields)

    try:
        fbAccounts = graph.get_object("me/accounts",fields=my_fields,appsecret_proof=app_secret_proof)

        ## print(accounts)
        for account in fbAccounts['data']:
            print(account['id']+';'+account['name'])
    except Exception as e:
        print(e)





#getAccount()
main()


