from typing import List
import discord
from peewee  import *
from Models.Database.tables import Squad, User, SquadMember
from serviceClients.tabStatsServiceClient import TabStatsServiceClient

class Repository:
    def addUser(self, usernames: List[str], message: discord.Message):
        tabServiceClient = TabStatsServiceClient()
        db = PostgresqlDatabase('r6bot', user='r6botclient', password='botPassword', port=5433)
        db.connect()
        squad = Squad.select().where(Squad.user_id == str(message.author.id))
        if not squad.exists():
            user = User.create(user_id = str(message.author.id), username = message.author.name)
            user.save()
            squad = Squad.create(user_id = str(message.author.id))
            squad.save()
        for username in usernames:
            ubisoftId = tabServiceClient.getPlayerProfileId(username)
            existingSquadMember = SquadMember.select().where(SquadMember.squad_member_ubisoft_id == ubisoftId, SquadMember.squad_id == squad)
            if not existingSquadMember.exists():
                newSquadMember = SquadMember.create(squad_id = squad, squad_member_username = username, squad_member_ubisoft_id = ubisoftId)
                newSquadMember.save()
        db.close()
        return

            