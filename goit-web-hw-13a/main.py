from fastapi import FastAPI
from src.conf.config import settings
from src.routes import contacts, auth, users
import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [ 
    "http://localhost:3000"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contacts.router, prefix='/api')
app.include_router(auth.router, prefix='/api')
app.include_router(users.router, prefix='/api')

@app.on_event("startup")
async def startup():
    r = await redis.Redis(host=settings.redis_host, port=settings.redis_port,password=settings.redis_password, db=0, encoding="utf-8",
                          decode_responses=True)
    await FastAPILimiter.init(r)

# @app.on_event("startup")
# async def startup():
#     await FastAPILimiter.init(app)


@app.get("/")
def read_root():
    return {"message": "Hello World"}





