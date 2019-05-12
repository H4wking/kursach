import http.client
import json
from api_shell import get_json


def player_profile(id):
    json_data = get_json("/tennis-t2/en/players/{}/profile.json?api_key=8vfgwpuch3rpnauqm9cbzp7d".format(id))
    profile = [json_data["player"]["id"], json_data["player"]["name"], surface_stats(json_data)]

    return profile


def surface_stats(data):
    stats = data["statistics"]["periods"]
    surfaces = {"Red clay": [0, 0], "Grass": [0, 0], "Hardcourt outdoor": [0, 0], "Hardcourt indoor": [0, 0]}

    for i in range(5):
        for surface in stats[i]["surfaces"]:
            surfaces[surface["type"]][0] += surface["statistics"]["matches_played"]
            surfaces[surface["type"]][1] += surface["statistics"]["matches_won"]

    for surface in surfaces:
        surfaces[surface] = round(surfaces[surface][1] / surfaces[surface][0], 3)

    return surfaces


data = player_profile("sr:competitor:14342")
print(data)
# print(json.dumps(data, indent=2))

