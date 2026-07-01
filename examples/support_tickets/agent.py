from orchestrapy import BaseAgentService, registry
from .schemas import TicketAnalysis
from pydantic import BaseModel

# Input schema
class TicketInput(BaseModel):
    description: str

# 1. Register a tool if needed (e.g., check account status)
@registry.register(name="get_user_status")
def get_user_status(user_id: str):
    return {"status": "premium"}

# 2. Define the service
class SupportTicketAgent(BaseAgentService[TicketInput, TicketAnalysis]):
    def __init__(self, agent_instance):
        super().__init__(agent_instance)