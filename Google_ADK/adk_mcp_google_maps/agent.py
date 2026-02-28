from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams, StreamableHTTPConnectionParams
from mcp import StdioServerParameters
import os
from dotenv import load_dotenv

load_dotenv()

google_maps_api_key = os.environ["GOOGLE_MAPS_API_KEY"]


MAPS_MCP_URL = "https://mapstools.googleapis.com/mcp" 

def get_maps_mcp_toolset():
    
    tools = MCPToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=MAPS_MCP_URL,
            headers={    
                "X-Goog-Api-Key": google_maps_api_key
            }
        )
    )
    print("MCP Toolset configured for Streamable HTTP connection.")
    return tools


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions related to locations,maps & directions',
    instruction='Answer user questions to the best of your knowledge ',
    tools=[ get_maps_mcp_toolset()])
"""
MCPToolset(
    connection_params=StdioConnectionParams(
        server_params = StdioServerParameters(
            command=r"C:\\Program Files\\nodejs\\npx.cmd",
            args=[
                "-y",
                "@modelcontextprotocol/server-google-maps",
            ],
            env={
                "GOOGLE_MAPS_API_KEY": google_maps_api_key
            }
        ),
    ),
    # You can filter for specific Maps tools if needed:
    # tool_filter=['get_directions', 'find_place_by_id']
) ],
"""