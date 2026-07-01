from pydantic import BaseModel, Field
from enum import Enum

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

class TicketAnalysis(BaseModel):
    priority: Priority
    classification: str = Field(description="Category of the ticket, e.g., Billing, Technical, Access")
    assignment_recommendation: str = Field(description="Which team should handle this ticket")
    resolution_suggestions: list[str] = Field(description="A list of 1-3 actionable steps to resolve")