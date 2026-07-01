from orchestrapy import BaseAgentService, registry
from pydantic import BaseModel

# 1. Define a contract
class TestInput(BaseModel):
    query: str

class TestOutput(BaseModel):
    result: str

# 2. Register a tool
@registry.register(name="test_tool")
def dummy_tool():
    return "Tool Works"

# 3. Simulate an Agent class
class MockAgent:
    async def run(self, data):
        # Mocking the PydanticAI Result
        class MockResult: data = TestOutput(result="Success")
        return MockResult()

# 4. Verify the binding
def test_framework():
    service = BaseAgentService(MockAgent())
    assert "test_tool" in service.tools
    print("✓ ToolRegistry Binding: PASSED")

if __name__ == "__main__":
    test_framework()