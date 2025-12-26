from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Base interface for all agents.
    """

    @abstractmethod
    def handle(self, query: str) -> str:
        pass
