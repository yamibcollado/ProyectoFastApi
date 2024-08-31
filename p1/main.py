from fastapi import FastAPI
from routers import user, producto

app = FastAPI()

app.include_router(user.router)
app.include_router(producto.router)


