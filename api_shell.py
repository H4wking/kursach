import http.client
import json


def get_json(source):
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", source)
    res = conn.getresponse()
    json_data = res.read().decode("utf-8")
    json_data = json.loads(json_data)
    return json_data


if __name__ == "__main__":
    json_data = get_json("/tennis-t2/en/matches/sr:match:8470986/summary.json?api_key=8vfgwpuch3rpnauqm9cbzp7d")
    json_data = json.dumps(json_data, indent=2)
    print(json_data)