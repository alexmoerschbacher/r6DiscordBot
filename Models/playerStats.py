class PlayerStats:
    def __init__(self, profileId, seasonYear, seasonNumber, matchesPlayed, roundsPlayed, matchesWon, matchesLost, roundsWon, roundsLost, kills, assists, death, kd, username):
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