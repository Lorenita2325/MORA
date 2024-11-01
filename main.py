from fastapi import FastAPI
from app.routes import router 

app = FastAPI( title="API Mora")

app.include_router(router)  
