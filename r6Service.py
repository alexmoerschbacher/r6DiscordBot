import json
import logging
from serviceClients.tabStatsServiceClient import TabStatsServiceClient
from serviceClients.r6ServiceClient import R6ServiceClient

class R6Service:
    def getCurrentSeasonStats(self):
        profiles = json.load(open('playerData/profiles.json'))
        uplayRequests = R6ServiceClient()
        tabStatsRequests = TabStatsServiceClient()
        try:
            preferredResults = tabStatsRequests.getPlayersStatsCurrentSeason(profiles)
            return preferredResults
        except Exception:
            logging.exception('tabStatsRequests is unavaliable: ')
            uplayResults = uplayRequests.getPlayersStatsCurrentSeason(profiles)
            return uplayResults

service = R6Service()

    