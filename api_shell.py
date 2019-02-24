import http.client

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/tennis-t2/en/players/sr:competitor:18111/versus/sr:competitor:15126/matches.xml?api_key=8vfgwpuch3rpnauqm9cbzp7d")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))