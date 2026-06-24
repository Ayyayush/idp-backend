from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from routes.upload import router as upload_router
from routes.extract import router as extract_router
from routes.summary import router as summary_router
from routes.chat import router as chat_router

app = FastAPI(
    title="IDP Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(extract_router)
app.include_router(summary_router)
app.include_router(chat_router)


@app.get("/")
def home():

    return {
        "message": "IDP Platform Running"
    }