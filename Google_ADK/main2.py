import os
from fastapi import FastAPI
from dotenv import load_dotenv
from google.adk.tools import google_search
from google.adk.runners

load_dotenv()

AGENT_DIR = "./agents"

SESSION_SERVICE_TYPE = os.getenv("SESSION_SERVICE_TYPE", "sqlite")
SESSION_DB_PATH = os.getenv("SESSION_DB_PATH", "./agent_sessions.db")

if SESSION_SERVICE_TYPE == "memory":
    SESSION_SERVICE_URI = "memory://"
else:
    SESSION_SERVICE_URI = f"sqlite:///{SESSION_DB_PATH}"

# Create ADK ASGI app
adk_app = create_app(
    agents_dir=AGENT_DIR,
    session_service_uri=SESSION_SERVICE_URI,
    web=True,
    trace_to_cloud=False,
)

# Mount into FastAPI
app = FastAPI(title="ADK + FastAPI")
app.mount("/", adk_app)

@app.get("/healthz")
def health():
    return {"status": "ok", "session_service": SESSION_SERVICE_TYPE}