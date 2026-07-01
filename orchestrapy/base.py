from abc import ABC
from typing import Generic, TypeVar, Dict, Callable, Optional
from pydantic import BaseModel
from fastapi import HTTPException
import logging
import uuid
from .registry import registry 
from .context import request_id_var

# Define generic types for strict type safety
InputSchema = TypeVar("InputSchema", bound=BaseModel)
OutputSchema = TypeVar("OutputSchema", bound=BaseModel)

class BaseAgentService(ABC, Generic[InputSchema, OutputSchema]):
    """
    Production-grade Base Service for PydanticAI agents.
    Features: Automated tool injection, structured logging, and request tracing.
    """
    def __init__(self, agent_instance):
        self.agent = agent_instance
        self.logger = logging.getLogger(self.__class__.__name__)
        # Register tools from the global registry
        self._tools = registry.get_tools()

    @property
    def tools(self) -> Dict[str, Callable]:
        return self._tools

    async def orchestrate(self, data: InputSchema, request_id: Optional[str] = None) -> OutputSchema:
        """
        Standardized orchestration pipeline with request tracing and error masking.
        """
        # Initialize request tracing
        trace_id = request_id or str(uuid.uuid4())
        token = request_id_var.set(trace_id)
        
        try:
            self.logger.info(f"[{trace_id}] Processing {data.__class__.__name__} request.")
            
            # Dynamic Tool Binding: Ensure the agent has the latest registry tools
            self.agent.tools = self._tools
            
            # Execute agent logic
            result = await self.agent.run(data)
            return result.data
            
        except ValueError as ve:
            # Catch validation errors (Business logic failures)
            self.logger.warning(f"[{trace_id}] Validation error: {ve}")
            raise HTTPException(status_code=422, detail=str(ve))
            
        except Exception as e:
            # Catch unexpected system failures, masking technical details from end-users
            self.logger.error(f"[{trace_id}] System failure: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail="Internal Orchestration Error")
            
        finally:
            # Cleanup context to prevent memory leaks in async tasks
            request_id_var.reset(token)