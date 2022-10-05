import json
from r6ServiceClient import R6ServiceClient

class R6Service:
    def getCurrentSeasonStats(self):
        profiles = json.load(open('playerData/profiles.json'))
        requests = R6ServiceClient()
        results = requests.getPlayersStatsCurrentSeason(profiles)
        return results

service = R6Service()

    