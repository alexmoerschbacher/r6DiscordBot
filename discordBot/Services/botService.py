import logging
from Models.playerStats import PlayerStats
from Repository.repository import Repository
from discordBot.Services.chartService import ChartService
from r6Service import R6Service
import discord

NOSQUADMATES = "It loooks like you're lacking squadmates why don't you add a squadmate using the /r6bot add user command first"
class BotService:
    
    def get_kd(stat: PlayerStats):
        return stat.kd
    
    def rankUs(message: discord.message):
        r6Service = R6Service()
        stats = list()
        try:    
            stats = r6Service.getCurrentSeasonStats(message)
            if len(stats) == 0:
                return NOSQUADMATES
            stats.sort(key=lambda stat: stat.kd, reverse=True)

            message = ''
            place = 1
            for stat in stats:
                message = message + str(place) + '. ' + stat.username + ' KD: ' + str(stat.kd) + '\n'
                place += 1
            return message            
        except:
            logging.exception('RankUs ran into an issue')
            return 'One of the APIs required for this command is down. Please try again later.'
    

    def mmr(message: discord.message):
        r6Service = R6Service()
        stats = list()
        try:
            stats = r6Service.getCurrentSeasonStats(message)
            if len(stats) == 0:
                return NOSQUADMATES
            stats.sort(key=lambda stat: stat.mmr, reverse=True)

            message = ''
            place = 1
            for stat in stats:
                message = message + str(place) + '. ' + stat.username + ' MMR: ' + str(stat.mmr) + '\n'
                place += 1
            return message
        except:
            return 'One of the APIs required for this command is down. Please try again later.'
    
    def charts(message: discord.message):
        r6Service = R6Service()
        stats = list()
        try:
            stats = r6Service.getCurrentSeasonStats(message)
            if len(stats) == 0:
                return NOSQUADMATES
            stats.sort(key = lambda stat: stat.mmr, reverse=True)
            username = []
            kills = []
            deaths = []
            colors = []
            for stat in stats:
                username.append(stat.username)
                kills.append(stat.kills)
                deaths.append(stat.death)
                if len(colors) == 0:
                    colors.append('green')
                else:
                    colors.append('orange')
            if len(colors) > 1:
                colors[-1] = 'red'
            chartService = ChartService()
            return chartService.killChart(username, kills, colors)
        except:
            logging.exception('Chart Service ran into an issue: ')
            return 'One of the APIs required for this command is down. Please try again later.'
    

    def help():
        return '/r6bot rankUs - Returns ranks in order of K/D \n /r6bot mmr - Returns ranks in order of mmr \n /r6bot kill chart - returns a chart displaying all kills \n /r6bot add user <username> - Adds a user to your squad (use their uplay name) \n /r6bot remove user <username> - Removes a user from your squad'
    
    def addUser(message: discord.Message):
        usernames = message.content.split()
        if len(usernames) < 3:
            return 'You need to provide the usernames of the users you want to add'
        usernames = usernames[3:]
        repository = Repository()
        repository = repository.addUser(usernames, message)
        return 'Users added sucessfully'

    def removeUser(message: discord.Message):
        usernames = message.content.split()
        if len(usernames) < 3:
            return 'You need to provide the usernames of the users you want to add'
        usernames = usernames[3:]
        repository = Repository()
        repository = repository.removeUser(usernames, message)
        return 'Users removed successfully'

    
    
        