import logging
from Models.playerStats import PlayerStats
from discordBot.Services.chartService import ChartService
from r6Service import R6Service


class BotService:
    
    def get_kd(stat: PlayerStats):
        return stat.kd
    
    def rankUs():
        r6Service = R6Service()
        stats = list()
        try:    
            stats = r6Service.getCurrentSeasonStats()
            stats.sort(key=lambda stat: stat.kd, reverse=True)

            message = ''
            place = 1
            for stat in stats:
                message = message + str(place) + '. ' + stat.username + ' KD: ' + str(stat.kd) + '\n'
            return message            
        except:
            return 'One of the APIs required for this command is down. Please try again later.'
    

    def mmr():
        r6Service = R6Service()
        stats = list()
        try:
            stats = r6Service.getCurrentSeasonStats()
            stats.sort(key=lambda stat: stat.mmr, reverse=True)

            message = ''
            place = 1
            for stat in stats:
                message = message + str(place) + '. ' + stat.username + ' MMR: ' + str(stat.mmr) + '\n'
                place += 1
            return message
        except:
            return 'One of the APIs required for this command is down. Please try again later.'
    
    def charts():
        r6Service = R6Service()
        stats = list()
        try:
            stats = r6Service.getCurrentSeasonStats()
            stats.sort(key = lambda stat: stat.mmr, reverse=True)
            username = []
            kills = []
            deaths = []
            for stat in stats:
                username.append(stat.username)
                kills.append(stat.kills)
                deaths.append(stat.death)
            chartService = ChartService()
            return chartService.killChart(username, kills)
        except:
            logging.exception('Chart Service ran into an issue: ')
            return 'One of the APIs required for this command is down. Please try again later.'

    
    
        