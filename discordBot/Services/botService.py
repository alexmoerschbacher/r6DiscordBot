from Models.playerStats import PlayerStats
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

            for stat in stats:
                message = message + 'Player: ' + stat.username + ' KD: ' + str(stat.kd) + '\n'
            return message            
        except:
            return 'One of the APIs required for this command is down. Please try again later.'
    
    
        