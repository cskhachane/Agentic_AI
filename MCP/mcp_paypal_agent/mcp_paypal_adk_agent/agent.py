from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams
from google.auth.transport.requests import Request
from google.oauth2 import id_token
import google.auth
import requests
import os


mcp_base_url = "http://127.0.0.1:8001"
mcp_url = f"{mcp_base_url}/mcp"

#credentials, _ = google.auth.default()

def get_paypal_token():
    client_id = os.getenv("PAYPAL_CLIENT_ID")
    secret = os.getenv("PAYPAL_SECRET")

    resp = requests.post(
        "https://api-m.sandbox.paypal.com/v1/oauth2/token",
        auth=(client_id, secret),
        data={"grant_type": "client_credentials"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    resp.raise_for_status()
    return resp.json()["access_token"]

access_token = get_paypal_token()
print(f"Access Token: {access_token}")


toolset = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=mcp_url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
    )
)

#id_token_val = id_token.fetch_id_token(auth_req, target_audience)
#print(f"ID Token: {id_token_val}")


root_agent = Agent(
    name="paypal_mcp_agent",
    model="gemini-2.5-flash",
    tools=[toolset],
    instruction="""
You are a PayPal client agent.
You can:
- Fetch PayPal access tokens
- Create orders using MCP tools

"""
)
