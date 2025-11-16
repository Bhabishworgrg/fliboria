from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse

from app.core.config import settings
from app.routes import auth


app = FastAPI(title=settings.TITLE)
api_router = APIRouter(prefix=settings.API_STR)

api_router.include_router(auth.router)

app.include_router(api_router)


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def root():
    return RedirectResponse('/docs') 
