import vertexai
from vertexai import agent_engines

vertexai.init(project="groovy-shore-484408-c5",location="us-central1")

agent_engine = agent_engines.create(
    display_name = "Memory_bank_demo"
    )

print(agent_engine.gca_resource.name)