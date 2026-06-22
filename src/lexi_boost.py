import json
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Bug:
    line: int
    column: int
    message: str

class LexiBoost:
    def __init__(self):
        self.bugs: List[Bug] = []

    def detect_bugs(self, code: str) -> List[Bug]:
        """
        Detect simple syntax errors: missing semicolons or colons at line ends.
        Returns a fresh list of Bug objects for each call.
        """
        self.bugs = []  # reset for each detection
        lines = code.split('\n')
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped == '':
                continue
            if not stripped.endswith(';') and not stripped.endswith(':'):
                # column is 1-indexed position of the end of the line
                column = len(line)
                self.bugs.append(Bug(i + 1, column, 'Missing semicolon'))
        return self.bugs

    def highlight_bugs(self, code: str, bugs: List[Bug]) -> str:
        """
        Append a comment with the bug message to each affected line.
        Handles empty code gracefully.
        """
        if not code:
            return ''
        lines = code.split('\n')
        for bug in bugs:
            # Ensure we don't go out of bounds
            if 1 <= bug.line <= len(lines):
                lines[bug.line - 1] += f'  # {bug.message}'
        return '\n'.join(lines)

    def get_tooltip(self, bug: Bug) -> str:
        """
        Return a formatted tooltip string for a Bug instance.
        Raises AttributeError if bug is None or missing attributes.
        """
        return f'Line {bug.line}, Column {bug.column}: {bug.message}'
