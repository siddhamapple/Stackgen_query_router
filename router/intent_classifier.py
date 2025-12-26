def classify_intent(query: str) -> str | None:
    """
    Classifies user intent based on keywords.
    Returns intent label or None.
    """
    query = query.lower()

    if "pull request" in query or "repo" in query or "github" in query:
        return "github"

    if "issue" in query or "ticket" in query or "linear" in query:
        return "linear"

    return None
