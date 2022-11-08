from Mappers.tabStatsProfileDataMapper import TabStatsProfileDataMapper
from requests import get
from cachetools import cached, TTLCache
class TabStatsServiceClient:
    def getPlayersStatsCurrentSeason(self, playerProfileIds):
        stats = list()
        for username, id in playerProfileIds.items():
            request = 'https://r6.apitab.net/website/profiles/' + id
            response = self.cacheAbleRequest(request)
            profileData = response.json()
            stats.append(TabStatsProfileDataMapper.tabStatsProfileDataStatsMapper(profileData, username))
        return stats
    

    @cached(TTLCache(maxsize=1024, ttl=600))
    def cacheAbleRequest(self, request, username=None):
        params = {}
        if username == None:
            params = {
                'update': 'true'
            }
        else:
            params['display_name'] = username
            params['platform'] = 'uplay'
        response = get(request, params = params)
        return response

    def getPlayerProfileId(self, username):
        request = 'https://r6.apitab.net/website/search'
        response = self.cacheAbleRequest(request, username)
        profileId = response.json()
        return profileId[0]['profile']["user_id"]