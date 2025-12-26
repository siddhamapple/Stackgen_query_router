from agents.base_agent import BaseAgent


class GitHubAgent(BaseAgent):
    """
    Mock agent for GitHub-related queries.
    """

    def handle(self, query: str) -> str:
        # Mocked response
        return "You have 2 open pull requests and 1 pending review."
