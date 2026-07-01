# orchestrapy/__init__.py

# 1. Import the core components from your internal modules
from .base import BaseAgentService
from .registry import registry
from .context import request_id_var

# 2. Define the public API using __all__
# This tells Python (and IDEs like VSCode) that ONLY these three items 
# are meant to be used by the external developer.
__all__ = [
    "BaseAgentService",
    "registry",
    "request_id_var"
]

# 3. Add package metadata
__version__ = "0.1.0"