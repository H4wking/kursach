from api_shell import get_json
import json
import time


def matches_from_tournaments(file):
    print(file)
    f = open(file).read()
    tournaments_list = json.loads(f)["tournaments"]
    matches = []
    try:
        for i in range(20):
            json_data = get_json("/tennis-t2/en/tournaments/{}/schedule.json?api_key=rzx3rjfpscjz2n724zf46n32".format(tournaments_list[i]["id"]))
            tour_matches = [i["id"] for i in json_data["sport_events"]]
            for match in tour_matches:
                matches.append(match)
            print(matches)
            time.sleep(1)
    except json.decoder.JSONDecodeError:
        pass
    return matches


data = matches_from_tournaments("women_tournaments.txt")
ids = ""
for id in data:
    ids += id + "\n"
with open("women_matches.txt", "w+") as file:
    file.write(ids)
