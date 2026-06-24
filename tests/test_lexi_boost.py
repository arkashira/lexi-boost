import pytest
from src.lexi_boost import PullRequest, Suggestion, review_pull_request, post_review_comment

def test_review_pull_request_refactor():
    pr = PullRequest(1, "2022-01-01T00:00:00Z", "def long_function(): pass")
    suggestions = review_pull_request(pr)
    assert len(suggestions) == 1
    assert suggestions[0].type == "refactor"
    assert suggestions[0].message == "Consider breaking down long functions into smaller ones"

def test_review_pull_request_security():
    pr = PullRequest(1, "2022-01-01T00:00:00Z", "password = 'secret'")
    suggestions = review_pull_request(pr)
    assert len(suggestions) == 1
    assert suggestions[0].type == "security"
    assert suggestions[0].message == "Avoid hardcoding sensitive information like passwords"

def test_review_pull_request_style():
    pr = PullRequest(1, "2022-01-01T00:00:00Z", "print('Hello World')")
    suggestions = review_pull_request(pr)
    assert len(suggestions) == 1
    assert suggestions[0].type == "style"
    assert suggestions[0].message == "Consider using a logging framework instead of print statements"

def test_post_review_comment():
    pr = PullRequest(1, "2022-01-01T00:00:00Z", "def long_function(): pass")
    suggestions = [Suggestion("refactor", "Consider breaking down long functions into smaller ones")]
    comment = post_review_comment(pr, suggestions)
    assert comment == "Review comment for PR 1:\n- refactor: Consider breaking down long functions into smaller ones\n"

def test_post_review_comment_empty_suggestions():
    pr = PullRequest(1, "2022-01-01T00:00:00Z", "")
    suggestions = []
    comment = post_review_comment(pr, suggestions)
    assert comment == "Review comment for PR 1:\n"
