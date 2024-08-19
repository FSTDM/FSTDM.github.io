# https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28
# HTTP request do not update the latest version, as quickly as using HTTP Github API
import base64
import json
import urllib.request
print("[API FETCH]\n * downloading")
url = "https://api.github.com/repos/FSTDM/WBP/contents/index.py"
response = urllib.request.urlopen(url).read()
jsonData = json.loads(response)
filecontent = jsonData["content"]
filedecoded = base64.b64decode(filecontent)
print(" * executing\n[API FETCH] DONE!\n")
exec(filedecoded)
