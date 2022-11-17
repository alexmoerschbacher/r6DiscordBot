import os
from typing import List
import discord
from peewee  import *
from Models.Database.tables import Squad, User, SquadMember
from serviceClients.tabStatsServiceClient import TabStatsServiceClient
from dotenv import load_dotenv
load_dotenv()
class Repository:

    def __init__(self):
        self.db = PostgresqlDatabase(os.getenv('DBSCHEMA'), user=os.getenv('DBUSERNAME'), password=os.getenv('DBPASSWORD'), port=os.getenv('DBPORT'))
        self.tabServiceClient = TabStatsServiceClient()

    def addUser(self, usernames: List[str], message: discord.Message):
        self.db.connect()
        squad = Squad.select().where(Squad.user_id == str(message.author.id))
        if not squad.exists():
            user = User.create(user_id = str(message.author.id), username = message.author.name)
            user.save()
            squad = Squad.create(user_id = str(message.author.id))
            squad.save()
        for username in usernames:
            ubisoftId = self.tabServiceClient.getPlayerProfileId(username)
            existingSquadMember = SquadMember.select().where(SquadMember.squad_member_ubisoft_id == ubisoftId, SquadMember.squad_id == squad)
            if not existingSquadMember.exists():
                newSquadMember = SquadMember.create(squad_id = squad, squad_member_username = username, squad_member_ubisoft_id = ubisoftId)
                newSquadMember.save()
        self.db.close()
        return
    
    def removeUser(self, usernames: List[str], message: discord.Message):
        self.db.connect()
        squad = Squad.select().where(Squad.user_id == str(message.author.id))
        if not squad.exists():
            return
        for username in usernames:
            ubisoftId = self.tabServiceClient.getPlayerProfileId(username)
            SquadMember.delete().where(SquadMember.squad_member_ubisoft_id == ubisoftId, SquadMember.squad_id == squad).execute()
        self.db.close()
        return
    
    def getSquadMembers(self, message: discord.Message):
        self.db.connect()
        squad = Squad.select().where(Squad.user_id == str(message.author.id))
        squadMembers = SquadMember.select().where(SquadMember.squad_id == squad)
        return squadMembers
