# OrchestraPy 

**OrchestraPy** is an enterprise-grade framework for building type-safe, contract-first Agentic AI microservices in Python.

[![PyPI Version](https://img.shields.io/pypi/v/orchestrapy.svg)](https://pypi.org/project/orchestrapy/)
[![Python Version](https://img.shields.io/pypi/pyversions/orchestrapy.svg)](https://pypi.org/project/orchestrapy/)

## The Problem
Most agent frameworks treat LLM output as a "suggestion." In mission-critical enterprise environments—like supply chain demand forecasting or automated complaint analysis—this unpredictability is a liability. Existing frameworks often sacrifice structural integrity for conversational flexibility.

## The Solution: OrchestraPy
OrchestraPy acts as a strict **Data-Contract Firewall** between your business logic and the Large Language Model. Built on top of `PydanticAI`, it enforces structure.

* **Contract-First:** Every agent interaction is governed by strict Pydantic schemas.
* **Stateless Microservices:** Optimized for scalable, audit-ready, stateless FastAPI deployments.
* **Deterministic Tool-Calling:** Forces agents to use deterministic Python tools rather than hallucinating mathematical outputs.
* **Built-in Auditability:** Asynchronous request tracing using `contextvars` ensures every AI decision can be tracked in production logs.

---

## ⚡ Quick Start: The "Golden Path"
If you are starting a new project and want to hit the ground running with a pre-configured, production-ready structure, use our official template. This generates the folder structure, FastAPI boilerplate, and core schemas in 5 seconds.

```bash
pip install cookiecutter
cookiecutter gh:sentomas/orchestrapy-template