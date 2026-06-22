import json
from dataclasses import dataclass
from typing import List

@dataclass
class CodeSnippet:
    language: str
    code: str

class LexiBoost:
    def __init__(self):
        self.code_snippets = []

    def add_code_snippet(self, language, code):
        self.code_snippets.append(CodeSnippet(language, code))

    def get_code_snippets(self, language=None):
        if language:
            return [snippet for snippet in self.code_snippets if snippet.language == language]
        return self.code_snippets

    def generate_documentation(self, language):
        snippets = self.get_code_snippets(language)
        if not snippets:
            return "No code snippets found for this language"
        return "\n".join([f"### {snippet.language}\n{snippet.code}" for snippet in snippets])

    def detect_bugs(self, code):
        # Simple bug detection: check for syntax errors
        try:
            compile(code, "", "exec")
            return "No bugs detected"
        except SyntaxError:
            return "Bug detected: syntax error"

    def complete_code(self, code, language):
        # Simple code completion: add a print statement
        return code + f"\nprint('Completed code in {language}')"
