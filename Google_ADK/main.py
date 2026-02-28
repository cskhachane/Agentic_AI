import os
from fastapi import FastAPI
from dotenv import load_dotenv
from google.adk.cli.fast_api import get_fast_api_app

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AGENT_DIR = BASE_DIR

SESSION_SERVICE_TYPE = os.getenv("SESSION_SERVICE_TYPE", "sqlite")
SESSION_DB_PATH = os.getenv("SESSION_DB_PATH", "./agent_sessions.db")

if SESSION_SERVICE_TYPE == "memory":
    SESSION_SERVICE_URI = "memory://"
else:
    SESSION_SERVICE_URI = f"sqlite:///{SESSION_DB_PATH}"

print("Agents dir:", AGENT_DIR)
print("Using session service:", SESSION_SERVICE_URI)

app: FastAPI = get_fast_api_app(
    agents_dir=AGENT_DIR,
    session_service_uri=SESSION_SERVICE_URI,
    allow_origins=["*"],
    web=True,
    trace_to_cloud=False,
    memory_service_uri="agentengine://projects/504822835633/locations/us-central1/reasoningEngines/5160591909827117056"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0" ,port=8080)