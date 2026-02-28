# not supported in google-adk 1.25.1 version
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.sessions import FirestoreSessionService

session_service = FirestoreSessionService(
    project_id="groovy-shore-484408-c5",
    collection="adk_sessions"
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[google_search],
    session_service=session_service
)

