'''
Author: gnarcap
Description: Script to restore the latest saved configuration to your router,
with an option to manually pass a configuration file name.
'''


'''
POST /html/conn_status_box.cmd HTTP/1.1
Host: 192.168.0.1
Content-Length: 0
Accept: */*
X-Requested-With: XMLHttpRequest
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Origin: http://192.168.0.1
Referer: http://192.168.0.1/html/index.html
Accept-Encoding: gzip, deflate, br
Cookie: toptab=ut; record_page=ut%2C%23utilities_configurationsave; CLINK_SESSION_ID=10digits; Authorization=base64str=
Connection: keep-alive


POST /html/utilities/utilities_configurationsave.cgi?sessionKey=10digits HTTP/1.1
Host: 192.168.0.1
Content-Length: 208479
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
Origin: http://192.168.0.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7nUzBnhYFVBemA8q
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://192.168.0.1/html/utilities/utilities_configurationsave_fileupload.html
Accept-Encoding: gzip, deflate, br
Cookie: toptab=ut; record_page=ut%2C%23utilities_configurationsave; CLINK_SESSION_ID=10digits; Authorization=base64str=
Connection: keep-alive


Body parameter:
"file_restore_field": <contents of .conf file>
------WebKitFormBoundary~~~
Content-Disposition: form-data; name="file_restore_field"; filename="router_original_844GConfig-2025-07-13.conf"
Content-Type: application/octet-stream



----
POST /html/saupdate2.cmd HTTP/1.1
Host: 192.168.0.1
Content-Length: 19
Accept: */*
X-Requested-With: XMLHttpRequest
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://192.168.0.1
Referer: http://192.168.0.1/html/index.html
Accept-Encoding: gzip, deflate, br
Cookie: toptab=ut; record_page=ut%2C%23utilities_configurationsave; CLINK_SESSION_ID=10digits; Authorization=base64str=
Connection: keep-alive

action=getLastError
'''

import requests as req 
import sys


# Find config file
# Upload to router - sessionKey?


ROUTER_IP=sys.argv[1:]
upload_data = {
    "Cookie": f"Authorization {b64str}",
    "Origin": f"http://{ROUTER_IP}",
    "Referer": f"http://{ROUTER_IP}/html/index.html",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary7nUzBnhYFVBemA8q",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Connection": "keep-alive",
    "file_restore_field": file_picker()
}

def file_picker():
    with open('file.pdf', 'rb') as f:
        data = f.read()
    return data

# TODO pull dynamic session key
p = req.post(f"http://{ROUTER_IP}/html/utilities/utilities_configurationsave.cgi?sessionKey={SESSION_KEY}")