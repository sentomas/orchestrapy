# Examples

## Support Ticket Analysis Agent
This example demonstrates how to transform unstructured customer complaints into structured data.

### Overview
- **Pattern**: Data Contract Enforcement
- **Input**: `TicketInput` (description: str)
- **Output**: `TicketAnalysis` (priority, classification, etc.)

### Usage
To run the agent locally, import the `SupportTicketAgent` class and bind it to your existing PydanticAI instance:

```python
from examples.support_tickets.agent import SupportTicketAgent
from examples.support_tickets.schemas import TicketInput

service = SupportTicketAgent(your_agent_instance)
result = await service.orchestrate(TicketInput(description="My internet is down!"))
print(result.priority) # Output: 'urgent'