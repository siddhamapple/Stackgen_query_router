from typing import Optional

# Simple keyword scoring for intent detection
INTENT_KEYWORDS = {
    "github": [
        "pull request",
        "pull requests",
        "pr",
        "prs",
        "commit",
        "repository",
        "repo",
        "github",
    ],
    "linear": [
        "issue",
        "issues",
        "ticket",
        "tickets",
        "bug",
        "assigned",
        "linear",
    ],
}


def classify_intent(query: str) -> Optional[str]: #return either string or none
    """
    Classifies the intent of a user query using keyword scoring.

    Returns:
        - intent string if matched
        - None if no intent matches
    """
    query = query.lower()
    scores = {}

    for intent, keywords in INTENT_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in query)
        if score > 0:
            scores[intent] = score

    if not scores:
        return None

    # Return intent with highest score
    return max(scores, key=scores.get)
