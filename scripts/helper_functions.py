# This sample source code is offered only as an example of what can or might be built using the IICS Github APIs, 
# and is provided for educational purposes only. This source code is provided "as-is" 
# and without representations or warrantees of any kind, is not supported by Informatica.
# Users of this sample code in whole or in part or any extraction or derivative of it 
# assume all the risks attendant thereto, and Informatica disclaims any/all liabilities 
# arising from any such use to the fullest extent permitted by law.

### This file contains helper functions used throughout the iics promotion pipeline

import requests

def iics_login(login_domain, iics_username, iics_password):

    URL = "https://dm-us.informaticacloud.com/saas/public/core/v3/login"
    BODY = {"username": iics_username,"password": iics_password}

    r = requests.post(url = URL, json = BODY)

    if r.status_code != 200:
        print("Caught exception: " + r.text)

    # extracting data in json format
    data = r.json()

    # return sessionId
    return data['userInfo']['sessionId']