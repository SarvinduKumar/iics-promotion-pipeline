import requests
import os

URL = os.environ['IICS_POD_URL']
SESSION_ID = os.environ['sessionId']
GITHUB_SHA = os.environ['GITHUB_SHA']

HEADERS = {"Content-Type": "application/json; charset=utf-8", "INFA-SESSION-ID": SESSION_ID }
BODY = {"commitHash": GITHUB_SHA }

r = requests.post(URL + "/v3/pullByCommitHash", headers=HEADERS, json = BODY )

print(r.text)