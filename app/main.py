from fastapi import FastAPI, WebSocket, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from contextlib import asynccontextmanager
from app.core.config import Settings
from app.services.ml_pipeline import MLPipeline
from app.services.openai_service import OpenAIService
from app.services.game_theory import GameTheoryEngine

# Load settings
settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize services on startup
    MLPipeline.initialize_models()
    yield
    # Cleanup on shutdown
    MLPipeline.cleanup()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
openai_service = OpenAIService()
game_theory_engine = GameTheoryEngine()

@app.get("/")
async def root():
    return {"message": "AI Negotiation Assistant API"}

@app.websocket("/ws/negotiation/{session_id}")
async def negotiation_websocket(websocket: WebSocket, session_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            # Process the negotiation data
            analysis = await MLPipeline.process_realtime_data(data)
            await websocket.send_json(analysis)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close() 