from typing import List
from requests import get
from Mappers.r6ProfileDataMapper import R6ProfileDataMapper

from Auth.auth import Auth
class R6ServiceClient:
    def getPlayersStatsCurrentSeason(self, playerProfileIds):
        auth = Auth.getAuth(self)
        headers = {
        'authorization': auth.authorization,
        'expiration': auth.expiration,
        'ubi-sessionid': auth.sessionId,
        'spaceId': auth.spaceId
    }

        params = {
            'spaceId': '5172a557-50b5-4665-b7db-e3f2e8c5041d',
            'view': 'seasonal',
            'aggregation': 'summary',
            'gameMode': 'casual',
            'platform': 'PC',
            'seasons': 'Y7S3',
        }
        stats = list()
        for username, id in playerProfileIds.items():
            response = get('https://prod.datadev.ubisoft.com/v1/profiles/' + id + '/playerstats', params=params, headers=headers)
            profileData = response.json()
            stats.append(R6ProfileDataMapper.r6ProfileDataPlayerStatsMapper(profileData, username))
        
        return stats


