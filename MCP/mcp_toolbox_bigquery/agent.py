import asyncio
from google.adk.agents import Agent
from toolbox_core import ToolboxClient

async def get_root_agent():
    async with ToolboxClient("http://127.0.0.1:5000") as toolbox_client:
        tools = await toolbox_client.load_toolset("my-toolset")

    prompt = """
    You're a helpful hotel assistant. You handle hotel searching, booking and
    cancellations. When the user searches for a hotel, mention it's name, id,
    location and price tier. Always mention hotel ids while performing any
    searches. This is very important for any operations. For any bookings or
    cancellations, please provide the appropriate confirmation. Be sure to
    update checkin or checkout dates if mentioned by the user.
    Don't ask for confirmations from the user.
    """

    return Agent(
        model="gemini-2.5-flash",
        name="hotel_agent",
        description="A helpful AI assistant that can search and book hotels.",
        instruction=prompt,
        tools=tools,
    )

root_agent = get_root_agent
