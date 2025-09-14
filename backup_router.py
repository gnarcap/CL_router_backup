'''
Author: gnarcap
Description: Script to save the current router configuration
'''

import requests as req
from . import auth as aa
import sys


ROUTER_IP=sys.argv[1:]
print(f"[+] Starting router backup script for {ROUTER_IP}")

req_data = {
    "Cookie": f"Authorization={aa.creds}",
    "Host": ROUTER_IP,
    "Referer": f"http://{ROUTER_IP}/html/index.html"
}

r = req.get(f"http://{ROUTER_IP}/html/utilities/backupsettings.conf", headers=req_data,stream=True)
content_disposition = r.headers.get("Content-Disposition")

cd_name_key = "filename="
cd_name_start = content_disposition.find(cd_name_key)
cfg_file = content_disposition[(cd_name_start+len(cd_name_key)):]

with open(cfg_file, "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)