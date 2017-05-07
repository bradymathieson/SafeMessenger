'''
api_connect.py interacts with the SafeMessenger server, live at:
http://safe-messenger-server.herokuapp.com

To see a list of current users in a session, navigate to:
http://safe-messenger-server.herokuapp.com/v1/current_users

Not sure how secure this server is... that's next on the list!
'''

import requests
import json

BASE_URL = "http://safe-messenger-server.herokuapp.com/v1"
TEST_BASE = "http://127.0.0.1:5000/v1"
HEADERS = {'Content-Type': 'application/json'}

def add_user(username, ip, port):
    post_data = {
        "username" : username,
        "ip" : ip,
        "port" : port
    }

    req = requests.post(TEST_BASE+"/add_user", data=json.dumps(post_data), headers=HEADERS)

    if req.status_code == 400:
        raise Exception("Error: " + req.text)

def remove_user(username, ip, port):
    post_data = {
        "username" : username,
        "ip" : ip,
        "port" : port
    }

    req = requests.post(TEST_BASE+"/remove_user", data=json.dumps(post_data), headers=HEADERS)

    if req.status_code == 400:
        raise Exception("Error: " + req.text)
