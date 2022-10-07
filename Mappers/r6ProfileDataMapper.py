from Models.playerStats import PlayerStats


class R6ProfileDataMapper:
    def r6ProfileDataPlayerStatsMapper(profileData, username):
        profileId = profileData['profileId']
        profileData = profileData['platforms']['PC']['gameModes']['casual']['teamRoles']['all'][0]
        return PlayerStats(profileId, profileData['seasonYear'], profileData['seasonNumber'], profileData['matchesPlayed'], profileData['roundsPlayed'], profileData['matchesWon'], profileData['matchesLost'], profileData['roundsWon'], profileData['roundsLost'], profileData['kills'], profileData['assists'], profileData['death'], profileData['killDeathRatio']['value'], username)
