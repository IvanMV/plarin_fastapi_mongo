from fastapi import FastAPI
from server.db.database import init_db
from server.routes.route_employees import router as Router


app = FastAPI()
app.include_router(Router, tags=["Список сотрудников"], prefix="")


@app.on_event("startup")
async def start_db():
    await init_db()
