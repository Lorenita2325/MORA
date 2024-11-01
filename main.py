from fastapi import FastAPI
from app.routes import router  # Asegúrate de que esto es correcto y de que tienes un archivo `routes.py` con los enrutadores

app = FastAPI()

app.include_router(router)  # Incluye tus rutas definidas en el archivo `routes.py`
