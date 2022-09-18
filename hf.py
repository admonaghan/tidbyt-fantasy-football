import requests
import json

LEAGUE_ID = 604106

HISTORIC_ESPN_URL = "https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/604106?seasonId=2021"
CURRENT_ESPN_URL  = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/2022/segments/0/leagues/604106"

PRIVATE_KEY = {
    "swid": "{97CD44DE-42B5-46E3-896B-8D8DDFE860A0}",
    "espn_s2": "AEBORFl92vtqoqrcpC5%2Bir7ynbSTTEzJmlg4QXMFwEs7iw7DQCZyM%2BZtqnkKLNcj07iikcvt0%2BqDubfeVou73QgSj4FtCFXfMF7PqNohDoI57FkxSZhuEOzG1%2BXOq0xC74n%2FRYmbvWAMT64gNN%2FZ%2F43Fi5kXaoJC66EJvTuk2uH03zAwAYK21wj0hoq%2FAqXTvDuBOZxQ88eSJBam5hFE3vd4OqsWQUKEWNqkiCrwwHHX0hE5GPGY1IhIAAqCPFTVlb40SQoRjyGDVs5X4fWH6fwlJ%2BHPsIjN24EaZ5eaxI22ZA%3D%3D"
}

'''
views
"mMatchup",
"mBoxscore",
"mMatchupScore",
"mRoster",
"mSettings",
"mStatus",
"mTeam",
"modular",
'''

PAYLOAD = {"view": [
    "mMatchupScore"
    ]
}

SINGLE_PAYLOAD = {"view": "mTeam"}
 

'''pulls all data for each current year'''

r = requests.get(HISTORIC_ESPN_URL, cookies=PRIVATE_KEY, params=PAYLOAD)
data = r.json()[0]["schedule"]
print(data)
