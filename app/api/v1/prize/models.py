from tortoise import fields
from tortoise.models import Model
from datetime import date

class Player(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    first_login = fields.DatetimeField(auto_now_add=True)
    last_login = fields.DateField(null=True) 
    score = fields.IntField(default=0)
    boosts: fields.ReverseRelation["PlayerBoost"]


    async def login(self):
        today = date.today()
        if self.last_login != today: 
            self.last_login = today
            self.score += 10
            await self.save()
        return self.score()
    

class Boost(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)
    boost_type = fields.CharField(max_length=50)
    value = fields.IntField()


class PlayerBoost(Model):
    id = fields.IntField(pk=True)
    player = fields.ForeignKeyField('models.Player', related_name='boosts')
    boost = fields.ForeignKeyField('models.Boost')
    acquired = fields.DatetimeField(auto_now_add=True)


class Level(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    order = fields.IntField(default=0)


class Prize(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)


class PlayerLevel(Model):
    id = fields.IntField(pk=True)
    player = fields.ForeignKeyField('models.Player',related_name='levels')
    level = fields.ForeignKeyField('models.Level')
    completed = fields.DatetimeField(null=True)
    is_completed = fields.BooleanField(default=False)
    score = fields.IntField(default=0)


class LevelPrize(Model):
    id = fields.IntField(pk=True)
    level = fields.ForeignKeyField('models.Level', related_name='prizes')
    prize = fields.ForeignKeyField('models.Prize')
    received = fields.DatetimeField(auto_now_add=True)