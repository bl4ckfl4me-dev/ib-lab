from routes.frontend import router as frontend_router
from routes.backend import router as backend_router
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import uvicorn


app = FastAPI()
app.mount('/static', StaticFiles(directory='src/static/'), name='static')
app.include_router(frontend_router)
app.include_router(backend_router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000, log_level='info')
