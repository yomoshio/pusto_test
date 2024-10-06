from app.api.v1.prize.models import Player, Level, Prize, PlayerLevel, LevelPrize


async def init_default_fields():
    
    player = await Player.create(username="test_player", score=0)
    print(f"Player created: {player}")


    level = await Level.create(title="Level 1", order=1)
    print(f"Level created: {level}")


    prize = await Prize.create(title="Prize 1")
    print(f"Prize created: {prize}")


    player_level = await PlayerLevel.create(player=player, level=level, completed="2023-10-05", is_completed=True, score=100)
    print(f"PlayerLevel created: {player_level}")


    level_prize = await LevelPrize.create(level=level, prize=prize, received="2023-10-05")
    print(f"LevelPrize created: {level_prize}")


   