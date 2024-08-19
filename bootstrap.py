import base64
import json
import urllib.request

print("[BOOTSTRAP] BEGIN")
url = "https://api.github.com/repos/FSTDM/WBP/contents/index.py"
print("\tdownloading")
response = urllib.request.urlopen(url).read()
jsonData = json.loads(response)
filecontent = jsonData["content"]
filedecoded = base64.b64decode(filecontent)
print("\t executing")
print("[BOOTSTRAP] END")
exec(filedecoded)
