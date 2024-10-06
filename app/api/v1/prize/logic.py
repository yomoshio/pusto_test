from services.export_to_csv import export_player_data 
from tortoise.transactions import in_transaction
from app.api.v1.prize.models import PlayerLevel, LevelPrize, Prize


async def assign_prize_to_player(player_id: int, level_id: int):
    async with in_transaction() as conn:
        player_level = await PlayerLevel.filter(player_id=player_id, level_id=level_id).first()

        if player_level and player_level.is_completed:
            level_prize = await LevelPrize.filter(level_id=level_id).first()

            if level_prize:
                player_level.received_prize_id = level_prize.prize_id

                await player_level.save(using_db=conn)

            else:
                raise ValueError("Приз для уровня не найден")
        
        else:
            raise ValueError("Уровень не пройден или запись не найдена")


async def handle_export_data(file_path: str):
    await export_player_data(file_path)


