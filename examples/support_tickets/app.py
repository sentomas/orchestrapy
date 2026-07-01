from fastapi import FastAPI, HTTPException
from .schemas import TicketInput, TicketAnalysis
from .agent import SupportTicketAgent
# Assume your PydanticAI agent is initialized here
from my_app.config import my_pydanticai_agent 

app = FastAPI(title="Support Ticket Orchestrator")

@app.post("/analyze-ticket", response_model=TicketAnalysis)
async def analyze(data: TicketInput, request_id: str = "default-id"):
    # Instantiate the agent service
    service = SupportTicketAgent(my_pydanticai_agent)
    
    # Call the orchestrate method with tracing
    return await service.orchestrate(data, request_id=request_id)