# OrchestraPy

**OrchestraPy** is an enterprise-grade framework for building type-safe, contract-first Agentic AI microservices. 

## The Problem
Most agent frameworks treat LLM output as a "suggestion." In mission-critical enterprise environments—like supply chain demand forecasting or automated complaint analysis—this unpredictability is a liability. Existing frameworks often sacrifice structural integrity for conversational flexibility.

## The Solution: OrchestraPy
OrchestraPy acts as a strict **Data-Contract Firewall** between your business logic and the LLM.
* **Contract-First:** Every agent interaction is governed by strict Pydantic schemas.
* **Stateless Microservices:** Optimized for scalable, audit-ready, stateless API deployments.
* **Deterministic Tool-Calling:** Forces agents to use deterministic Python tools rather than hallucinating mathematical outputs.

## Quick Start
1. **Install**: `pip install orchestrapy`
2. **Define**: Create your input/output schemas using Pydantic.
3. **Orchestrate**:
```python
from orchestrapy.base import BaseAgentService

class MyAgent(BaseAgentService[InputSchema, OutputSchema]):
    # Your agent logic here