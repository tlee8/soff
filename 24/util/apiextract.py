import urllib, json

url = "https://api.nasa.gov/planetary/apod?api_key=54FEbz3y1Hlprqa74pXDAQlA7mfqlrwCOlsTVK6D"

x = urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

w = json.loads(x)

print (w)
