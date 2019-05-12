from api_shell import get_json


def rankings(gender):
    """
    (str) -> lst
    :param gender: 0 for female rankings, 1 for male rankings
    :return: list containing rankings
    """
    json_data = get_json("/tennis-t2/en/players/rankings.json?api_key=8vfgwpuch3rpnauqm9cbzp7d")

    ranking = json_data["rankings"][gender]["player_rankings"]
    ranking_list = []

    for rank in ranking:
        ranking_list.append((rank["rank"], rank["player"]["id"], rank["player"]["name"]))

    return ranking_list


print(rankings(1))
