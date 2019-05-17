from api_shell import get_json
import json


def tournaments(file, gender):
    f = open("tournaments.txt").read()
    tournaments_list = json.loads(f)["tournaments"]
    result = [i for i in tournaments_list if i["gender"] == gender and i["type"] == "singles"]
    # for i in range(len(tournaments_list)):
    #     if (tournaments_list[i]["gender"] != gender and tournaments_list[i]["gender"] != "mixed") or tournaments_list[i]["type"] == "doubles":
    #         tournaments_list[i] = 0
    # while 0 in tournaments_list:
    #     tournaments_list.remove(0)
    result = {"tournaments": result}
    return result


data = tournaments("tournaments.txt", "women")
with open("women_tournaments.txt", "w+") as file:
    json.dump(data, file, indent=2)
