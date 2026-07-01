from contextvars import ContextVar
from typing import Optional

# This stores the request ID uniquely for the current async task
request_id_var: ContextVar[Optional[str]] = ContextVar("request_id", default=None)