import requests
import os
from base64 import b64encode
from nacl import encoding, public

URL = os.environ['IICS_LOGIN_URL']
USERNAME = os.environ['IICS_USERNAME']
PASSWORD = os.environ['IICS_PASSWORD']

URL = "https://dm-us.informaticacloud.com/saas/public/core/v3/login"
BODY = {"username": USERNAME,"password": PASSWORD}

r = requests.post(url = URL, json = BODY)

if r.status_code != 200:
    print("Caught exception: " + r.text)

# extracting data in json format
data = r.json()

os.environ['sessionId'] = data['userInfo']['sessionId']

print(os.listdir())

env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write("sessionId=" + data['userInfo']['sessionId'])


#public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
#sealed_box = public.SealedBox(public_key)
#encrypted = sealed_box.encrypt(data['userInfo']['sessionId'].encode("utf-8"))
#b64encode(encrypted).decode("utf-8")