from peewee  import *
import os
from dotenv import load_dotenv
load_dotenv()

db = PostgresqlDatabase(os.getenv('DBSCHEMA'), user=os.getenv('DBUSERNAME'), password=os.getenv('DBPASSWORD'), port=os.getenv('DBPORT'))

class User(Model):
    user_id = CharField(primary_key=True)
    username = CharField()

    class Meta:
        database = db
        schema = "r6bot"

class Squad(Model):
    squad_id = PrimaryKeyField()
    user_id = ForeignKeyField(User, backref = 'squads')

    class Meta:
        database = db
        schema = "r6bot"

class SquadMember(Model):
    squad_member_id = PrimaryKeyField()
    squad_id = ForeignKeyField(Squad, backref='squadmembers')
    squad_member_username = CharField()
    squad_member_ubisoft_id = CharField()

    class Meta:
        database = db
        schema = "r6bot"

db.connect()

db.create_tables([User, Squad, SquadMember])

#user = User.create(username ="Todd")
#user.save()