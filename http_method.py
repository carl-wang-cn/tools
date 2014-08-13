#! /usr/bin/python2.7
#coding=utf8

import httplib
import urllib
import urlparse

http_client = None
body = urllib.urlencode({"name":"carl", "age":27}, doseq=0)
#body = None
cookie = "name=carl; age=27; gendor=male"
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain",
           "Cookie": cookie}
url = "/test"
host = "localhost"
port = 8080
method = "POST"
#method = "GET"
#method = "HEAD"

try:
    ret = urlparse.urlparse(host)
    if ret.scheme == "https":
        http_client = httplib.HTTPSConnection(host, port, timeout=30)
    else:
        http_client = httplib.HTTPConnection(host, port, timeout=30)
    http_client.request(method, url, body, headers)

    response = http_client.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders()
except Exception, e:
    print e
finally:
    if http_client:
        http_client.close()
