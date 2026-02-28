import asyncio
import logging
import os
from fastmcp import FastMCP
import uuid
from dotenv import load_dotenv

load_dotenv()
log_level = os.getenv("LOG_LEVEL", "INFO")
port = int(os.getenv("PORT", "8080"))

# Configure logging
logger = logging.getLogger(__name__)
numeric_level = getattr(logging, log_level, logging.DEBUG)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=numeric_level)

# FastMCP setup

app = FastMCP()

@app.tool()
def create_order(product_name: str, quantity: int) -> dict:
    """
    create an order based on the inputs required form the user. Take inputs like product name, quantity.
    cost of each product will be $5.
    """
    total_cost = quantity * 5
    return {
        "status": "ok",
        "product": product_name,
        "quantity": quantity,
        "unit_price": 5,
        "total_cost": total_cost,
        "order_id": uuid.uuid4(),
        "currency": "USD",
        "message": "Order created successfully.",
    }


if __name__ == "__main__":
    logger.info(f"MCP server started on port {os.getenv('PORT', '8001')}")
    asyncio.run(
        app.run_async(
            transport="http",
            host="127.0.0.1",
            port=int(os.getenv("PORT", 8001))
        )
    )