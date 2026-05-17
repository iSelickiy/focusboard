from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/")
def root():
    return {'message': 'FocusBoard is alive'}

@router.get("/health")
def health_check():
    return {'Status': 'ok'}