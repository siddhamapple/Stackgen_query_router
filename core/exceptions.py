class RouterError(Exception):
    """Base exception for routing errors."""


class AgentNotFoundError(RouterError):
    """Raised when no suitable agent is found."""


class AgentExecutionError(RouterError):
    """Raised when an agent fails to process a query."""
