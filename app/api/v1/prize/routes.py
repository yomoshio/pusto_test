from fastapi import APIRouter, HTTPException
from app.api.v1.prize.logic import handle_export_data, assign_prize_to_player


router = APIRouter(prefix='/prize', tags=["game"])


@router.post("/assign_prize/")
async def assign_prize(player_id: int, level_id: int):
    try:
        await assign_prize_to_player(player_id, level_id)
        return {"message": "Prize assigned successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/export_csv/")
async def export_csv():
    file_path = "player_data.csv"
    await handle_export_data(file_path)
    return {"message": f"Data exported to {file_path}"} 