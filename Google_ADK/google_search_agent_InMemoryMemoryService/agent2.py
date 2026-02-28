from google.adk.agents.llm_agent import Agent
from google.adk.tools.preload_memory_tool import PreloadMemoryTool
from google.adk.memory import InMemoryMemoryService
from google.adk.sessions import InMemorySessionService
from google.adk.app import App

# Create services
memory_service = InMemoryMemoryService()
session_service = InMemorySessionService()

# Tool
preload_memory_tool = PreloadMemoryTool()

# Auto-save callback
async def auto_save_session_to_memory_callback(callback_context):
    invocation_context = callback_context.invocation_context

    await invocation_context.memory_service.add_session_to_memory(
        invocation_context.session_id
    )
    print("Session saved to memory")

# Agent (NO memory_service here)
root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A helpful assistant",
    instruction="Answer user questions",
    tools=[preload_memory_tool],
    after_agent_callback=auto_save_session_to_memory_callback
)


app = App(
    agents=[root_agent],
    session_service=session_service,
    memory_service=memory_service
)