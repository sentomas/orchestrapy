from typing import Callable, Dict, Optional

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    # Explicitly use Optional[str] for the default parameter
    def register(self, name: Optional[str] = None):
        def decorator(func: Callable):
            tool_name = name or func.__name__
            if tool_name in self._tools:
                raise ValueError(f"Tool '{tool_name}' already registered!")
            self._tools[tool_name] = func
            return func
        return decorator

    def get_tools(self) -> Dict[str, Callable]:
        return self._tools

registry = ToolRegistry()