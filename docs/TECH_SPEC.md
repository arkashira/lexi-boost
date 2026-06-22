```markdown
# TECH SPEC: Lexi Boost

## Overview

Lexi Boost is a VS Code extension designed to provide intelligent inline code completion for Python, Go, and TypeScript. It leverages advanced language models and contextual analysis to deliver accurate and relevant code suggestions with minimal latency.

## Architecture Overview

### High-Level Components

1. **Extension Host** - Core VS Code extension framework
2. **Completion Provider** - Registers with VS Code's completion system
3. **Language Server** - Processes language-specific parsing and analysis
4. **Model Inference Engine** - Handles LLM-based code completion
5. **Context Manager** - Maintains and updates context window
6. **Cache Layer** - Stores recent completions and patterns
7. **Configuration Service** - Manages user preferences and settings

### Data Flow

```
User Types Code → Language Server Parses Context → Context Manager Updates Window → Model Inference Engine Generates Suggestions → Completion Provider Delivers to VS Code UI
```

## Components

### Extension Host
- Built using VS Code Extension API
- Implements `activate()` and `deactivate()` lifecycle methods
- Registers completion providers for supported languages
- Manages extension configuration and state

### Completion Provider
- Implements VS Code's `CompletionItemProvider` interface
- Triggers after 200ms of typing (configurable)
- Filters and formats completion suggestions
- Integrates with VS Code's UI for display

### Language Server
- Parses current file context using language-specific parsers
- Identifies scope, imports, and surrounding code structure
- Maintains context window for completion generation
- Handles multi-file context when applicable

### Model Inference Engine
- Utilizes vLLM for production inference engine
- Implements SGLang for structured generation
- Supports multiple model backends (local and remote)
- Handles batching and caching for performance optimization

### Context Manager
- Maintains sliding window of recent code context
- Tracks file position and scope boundaries
- Manages cross-file references and imports
- Ensures context relevance for completion generation

### Cache Layer
- Stores recent completion results for reuse
- Implements LRU eviction policy
- Caches common patterns and frequently used code snippets
- Reduces redundant inference requests

### Configuration Service
- Manages user preferences (delay, model selection, etc.)
- Persists settings to VS Code's configuration system
- Provides default values and validation
- Supports workspace-level overrides

## Data Model

### Completion Item Structure
```json
{
  "label": "function_name",
  "kind": "Function",
  "detail": "def function_name(param1: str, param2: int) -> None:",
  "documentation": "Description of function purpose",
  "insertText": "function_name(${1:param1}, ${2:param2})",
  "range": {
    "start": {"line": 10, "character": 5},
    "end": {"line": 10, "character": 15}
  },
  "additionalTextEdits": [
    {
      "range": {"start": {"line": 0, "character": 0}, "end": {"line": 0, "character": 0}},
      "newText": "import module\n"
    }
  ]
}
```

### Context Window Structure
```json
{
  "file_path": "/path/to/file.py",
  "cursor_position": {"line": 15, "character": 10},
  "context_window": [
    {"line_number": 10, "content": "def example_function():"},
    {"line_number": 11, "content": "    pass"},
    {"line_number": 12, "content": ""},
    {"line_number": 13, "content": "# Current line being completed"},
    {"line_number": 14, "content": "    "},
    {"line_number": 15, "content": "    "},
    {"line_number": 16, "content": ""}
  ],
  "imports": ["import os", "from typing import List"],
  "scope": {
    "function": "example_function",
    "class": null,
    "module": "main"
  }
}
```

## Key APIs/Interfaces

### VS Code Extension API
- `vscode.languages.registerCompletionItemProvider()`
- `vscode.workspace.onDidChangeConfiguration()`
- `vscode.window.showInformationMessage()`
- `vscode.workspace.getConfiguration()`

### Extension Lifecycle
```typescript
export async function activate(context: vscode.ExtensionContext) {
    // Register completion providers for Python, Go, TypeScript
    const pythonProvider = new CompletionProvider('python');
    const goProvider = new CompletionProvider('go');
    const tsProvider = new CompletionProvider('typescript');
    
    context.subscriptions.push(
        vscode.languages.registerCompletionItemProvider('python', pythonProvider),
        vscode.languages.registerCompletionItemProvider('go', goProvider),
        vscode.languages.registerCompletionItemProvider('typescript', tsProvider)
    );
}

export function deactivate() {
    // Cleanup resources
}
```

### Model Inference Interface
```typescript
interface ModelInferenceEngine {
    generateCompletions(context: ContextWindow): Promise<CompletionItem[]>;
    setModel(modelName: string): void;
    getModelStatus(): ModelStatus;
}
```

## Tech Stack

### Core Technologies
- **Language**: TypeScript/JavaScript
- **Framework**: VS Code Extension API
- **Inference Engine**: vLLM (vllm-project/vllm)
- **Structured Generation**: SGLang (sgl-project/sglang)
- **Build System**: VS Code Extension Builder
- **Testing**: Jest, VS Code Test Runner

### Dependencies

#### Runtime Dependencies
```json
{
  "@types/vscode": "^1.80.0",
  "vscode-languageclient": "^9.0.0",
  "axios": "^1.4.0",
  "lodash": "^4.17.21"
}
```

#### Development Dependencies
```json
{
  "@types/jest": "^29.5.0",
  "@types/node": "^20.0.0",
  "jest": "^29.5.0",
  "ts-jest": "^29.1.0",
  "typescript": "^5.0.0",
  "@vscode/test-electron": "^2.3.0"
}
```

## Deployment

### VS Code Marketplace Distribution
1. Build extension package using `vsce package`
2. Publish to VS Code Marketplace using `vsce publish`
3. Versioning follows semantic versioning (MAJOR.MINOR.PATCH)
