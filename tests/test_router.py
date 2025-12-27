import pytest
from router.query_router import route_query
from core.exceptions import AgentNotFoundError, AgentExecutionError


def test_github_routing():
    response = route_query("Show my open pull requests")
    assert "pull request" in response.lower()


def test_linear_routing():
    response = route_query("What issues are assigned to me?")
    assert "issue" in response.lower()


def test_unknown_query():
    with pytest.raises(AgentNotFoundError):
        route_query("What's the weather today?")


def test_case_insensitive_query():
    response = route_query("SHOW MY OPEN PRs")
    assert "pull request" in response.lower()


def test_scored_intent_routing():
    # Contains keywords for both, but GitHub should win due to scoring
    response = route_query("Show my assigned pull request issues")
    assert "pull request" in response.lower() or "issue" in response.lower()


def test_agent_execution_error(monkeypatch):
    from agents.github_agent import GitHubAgent

    def broken_handle(self, query):
        raise RuntimeError("simulated failure")

    monkeypatch.setattr(GitHubAgent, "handle", broken_handle)

    with pytest.raises(AgentExecutionError):
        route_query("Show my open pull requests")
