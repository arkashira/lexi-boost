import json
from dataclasses import dataclass
from typing import List

@dataclass
class CompletionItem:
    label: str
    detail: str

class LexiBoost:
    def __init__(self):
        self.languages = ["python", "go", "typescript"]
        self.completion_items = {
            "python": [CompletionItem("print", "Prints output to the console")],
            "go": [CompletionItem("fmt.Println", "Prints output to the console")],
            "typescript": [CompletionItem("console.log", "Prints output to the console")],
        }

    def get_completion_items(self, language: str) -> List[CompletionItem]:
        return self.completion_items.get(language, [])

    def register_completion_provider(self, language: str):
        if language in self.languages:
            return f"Registered completion provider for {language}"
        else:
            raise ValueError(f"Unsupported language: {language}")

    def get_completion_suggestions(self, language: str, prefix: str) -> List[CompletionItem]:
        completion_items = self.get_completion_items(language)
        return [item for item in completion_items if item.label.startswith(prefix)]
