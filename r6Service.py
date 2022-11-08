import logging
from serviceClients.tabStatsServiceClient import TabStatsServiceClient
from serviceClients.r6ServiceClient import R6ServiceClient
import discord.message
from Repository.repository import Repository
class R6Service:
    def getCurrentSeasonStats(self, message: discord.message):
        uplayRequests = R6ServiceClient()
        tabStatsRequests = TabStatsServiceClient()
        repository = Repository()
        profiles = {}
        squadmembers = repository.getSquadMembers(message)
        for member in squadmembers:
            profiles[member.squad_member_username] = member.squad_member_ubisoft_id
        try:
            preferredResults = tabStatsRequests.getPlayersStatsCurrentSeason(profiles)
            return preferredResults
        except Exception:
            logging.exception('tabStatsRequests is unavaliable: ')
            uplayResults = uplayRequests.getPlayersStatsCurrentSeason(profiles)
            return uplayResults

service = R6Service()

    