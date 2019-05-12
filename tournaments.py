from api_shell import get_json
import json


def tournaments(file, gender):
    f = open("tournaments.txt").read()
    tournaments_list = json.loads(f)["tournaments"]
    print(len(tournaments_list))
    print(tournaments_list[0])
    for i in range(len(tournaments_list)):
        print(tournaments_list[i]["type"])
        print(tournaments_list[i]["type"] != "singles")
        if (tournaments_list[i]["gender"] != gender and tournaments_list[i]["gender"] != "mixed") or tournaments_list[i]["type"] == "doubles":
            tournaments_list[i] = 0
    while 0 in tournaments_list:
        tournaments_list.remove(0)
    print(len(tournaments_list))
    result = {"tournaments": tournaments_list}
    return result




            # "tournaments.txt"
data = tournaments("tournaments.txt", "men")
with open("men_tournaments.txt", "w+") as f:
    json.dump(data, f, indent=2)
