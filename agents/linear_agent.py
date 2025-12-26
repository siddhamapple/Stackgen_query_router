from agents.base_agent import BaseAgent


class LinearAgent(BaseAgent):
    """
    Mock agent for Linear-related queries.
    """

    def handle(self, query: str) -> str:
        return "You have 3 issues assigned to you in Linear."
