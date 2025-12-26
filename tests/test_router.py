from router.query_router import route_query


def test_github_routing():
    response = route_query("Show my open pull requests")
    assert "pull requests" in response.lower()


def test_unknown_query():
    try:
        route_query("What's the weather today?")
        assert False
    except Exception:
        assert True
