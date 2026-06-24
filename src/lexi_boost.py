import json
from dataclasses import dataclass
from datetime import datetime, timedelta
import argparse

@dataclass
class PullRequest:
    id: int
    created_at: str
    code: str

@dataclass
class Suggestion:
    type: str
    message: str

def review_pull_request(pr: PullRequest) -> list[Suggestion]:
    suggestions = []
    # Code refactoring suggestion
    if "long_function" in pr.code:
        suggestions.append(Suggestion("refactor", "Consider breaking down long functions into smaller ones"))
    # Security check suggestion
    if "password" in pr.code:
        suggestions.append(Suggestion("security", "Avoid hardcoding sensitive information like passwords"))
    # Style fix suggestion
    if "print" in pr.code:
        suggestions.append(Suggestion("style", "Consider using a logging framework instead of print statements"))
    return suggestions

def post_review_comment(pr: PullRequest, suggestions: list[Suggestion]) -> str:
    comment = f"Review comment for PR {pr.id}:\n"
    for suggestion in suggestions:
        comment += f"- {suggestion.type}: {suggestion.message}\n"
    return comment

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr", type=json.loads, help="Pull request data")
    args = parser.parse_args()
    pr = PullRequest(**args.pr)
    suggestions = review_pull_request(pr)
    comment = post_review_comment(pr, suggestions)
    print(comment)

if __name__ == "__main__":
    main()
