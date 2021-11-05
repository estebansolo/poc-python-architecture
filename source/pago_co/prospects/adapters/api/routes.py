from fastapi import APIRouter, status, Request, Response


router = APIRouter(prefix='/prospects', tags=["Prospects"])


@router.post('/prospect-evaluation', status_code=status.HTTP_200_OK)
async def prospect_evaluation(request: Request, response: Response):
    pass
