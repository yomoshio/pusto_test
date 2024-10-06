import pandas as pd
from app.api.v1.prize.models import PlayerLevel


async def export_player_data(file_path: str):
    player_levels = await PlayerLevel.all().prefetch_related('player', 'level')


    data = [{
        "player_id": pl.player.id,
        "level_title": pl.level.title,
        "is_complited": pl.is_completed,
        "score": pl.score,
    } for pl in player_levels]

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)