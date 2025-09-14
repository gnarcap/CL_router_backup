import os
import base64
import sys

def pull_creds_env():
    username=os.getenv("router_user")
    password=os.getenv("router_pass")
    b64str = base64.b64encode(f"{username}:{password}".encode('utf-8'))
    return b64str.decode('utf-8')

def pull_creds(user, passwd):
    b64str = base64.b64encode(f"{user}:{passwd}".encode('utf-8'))
    return b64str.decode('utf-8')


if __name__ != "__main__":
    creds = pull_creds(sys.argv[2:], sys.argv[3:])