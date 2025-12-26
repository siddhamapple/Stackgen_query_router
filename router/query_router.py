from agents.github_agent import GitHubAgent
from agents.linear_agent import LinearAgent
from core.exceptions import AgentNotFoundError, AgentExecutionError
from core.logger import setup_logger
from router.intent_classifier import classify_intent

logger = setup_logger("router")

AGENT_REGISTRY = {
    "github": GitHubAgent(),
    "linear": LinearAgent(),
}


def route_query(query: str) -> str:
    """
    Routes the query to the appropriate agent.
    """
    intent = classify_intent(query)

    if intent is None:
        logger.warning("No intent matched for query")
        raise AgentNotFoundError("No agent found for this query")

    agent = AGENT_REGISTRY.get(intent)

    if not agent:
        logger.error(f"No agent registered for intent: {intent}")
        raise AgentNotFoundError("Agent not registered")

    logger.info(f"Routing query to {agent.__class__.__name__}")

    try:
        return agent.handle(query)
    except Exception as e:
        logger.error(f"Agent execution failed: {e}")
        raise AgentExecutionError("Agent failed to process query")
