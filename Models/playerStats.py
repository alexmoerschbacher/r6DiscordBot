class PlayerStats:
    def __init__(self, profileId=None, seasonYear=None, seasonNumber=None, matchesPlayed=None, roundsPlayed=None, matchesWon=None, matchesLost=None, roundsWon=None, roundsLost=None, kills=None, assists=None, death=None, kd=None, username=None):
        self.profileId = profileId
        self.seasonYear = seasonYear
        self.seasonNumber = seasonNumber
        self.matchesPlayed = matchesPlayed
        self.roundsPlayed = roundsPlayed
        self.matchesWon = matchesWon
        self.matchesLost = matchesLost
        self.roundsWon = roundsWon
        self.roundsLost = roundsLost
        self.kills = kills
        self.assists = assists
        self.death = death
        self.kd = kd
        self.username = username