import requests

conn = requests.get("https://crumbs.web.actf.co")
resp = conn.content.decode()
print(resp)
while resp[:5] == "Go to":
    conn = requests.get("https://crumbs.web.actf.co/" + resp[6:])
    resp = conn.content.decode()
    print(resp)
