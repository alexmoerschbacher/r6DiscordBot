from peewee  import *

db = PostgresqlDatabase('r6bot', user='r6botclient', password='botPassword', port=5433)

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

print("SUCCESS")

db.execute_sql("SELECT * FROM USER")

#user = User.create(username ="Todd")
#user.save()