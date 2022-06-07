import requests
import os
import sys
import json
from helper_functions import iics_login
from helper_functions import iics_rollback_mapping

LOGIN_URL = os.environ['IICS_LOGIN_URL']
POD_URL =  os.environ['IICS_POD_URL']

UAT_IICS_USERNAME = os.environ['UAT_IICS_USERNAME']
UAT_IICS_PASSWORD = os.environ['UAT_IICS_PASSWORD']

PROJECT_NAME = os.environ['UAT_IICS_USERNAME']
MAPPING_TASK_NAME = os.environ['UAT_IICS_PASSWORD']

SESSION_ID = iics_login(LOGIN_URL, UAT_IICS_USERNAME, UAT_IICS_PASSWORD )

print(LOGIN_URL)

iics_rollback_mapping(POD_URL, SESSION_ID, PROJECT_NAME, MAPPING_TASK_NAME  )