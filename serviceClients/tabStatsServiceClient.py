from Mappers.tabStatsProfileDataMapper import TabStatsProfileDataMapper
from requests import get

class TabStatsServiceClient:
    def getPlayersStatsCurrentSeason(self, playerProfileIds):
        params = {
            'update': 'true'
        }

        stats = list()
        for username, id in playerProfileIds.items():
            response = get('https://r6.apitab.net/website/profiles/' + id, params = params)
            profileData = response.json()
            stats.append(TabStatsProfileDataMapper.tabStatsProfileDataStatsMapper(profileData, username))
        return stats