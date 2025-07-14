from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine, Base, get_db
from configs.routers import main_router
from configs.settings import settings
import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter


app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    # for rate limiting initialize it
    redis_conn =  redis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis_conn)

@app.get("/health-check")
def health_check():
    return {'message': "Health OK"}

# # Registering routes
app.include_router(main_router)