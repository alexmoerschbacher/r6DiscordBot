from Models.playerStats import PlayerStats

class TabStatsProfileDataMapper:
    def tabStatsProfileDataStatsMapper(profileData, username):
        profileId = profileData['profile']['profile_id']
        profileData = profileData["current_season_records"]["casual"]
        return PlayerStats(profileId, None, None, None, None, profileData["wins"], profileData["losses"], None, None, profileData["kills"], None, profileData["deaths"], profileData["kd"], username, profileData["mmr"])