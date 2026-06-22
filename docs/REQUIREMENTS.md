# Requirements for **lexi-boost**

> **Project**: lexi-boost  
> **Repository**: `lexi-boost`  
> **Scope**: VS Code extension that provides inline code completion for **Python**, **Go**, and **TypeScript**.  
> **Target Release**: v1.0.0 (first stable release on the VS Code Marketplace)

---

## 1. Functional Requirements

| ID | Description | Acceptance Criteria |
|----|-------------|---------------------|
| **FR‑1** | Register a completion provider for Python files. | The extension registers a `CompletionItemProvider` for `python` language on activation. |
| **FR‑2** | Register a completion provider for Go files. | The extension registers a `CompletionItemProvider` for `go` language on activation. |
| **FR‑3** | Register a completion provider for TypeScript files. | The extension registers a `CompletionItemProvider` for `typescript` language on activation. |
| **FR‑4** | Trigger completions after 200 ms of idle typing. | The provider is invoked only if the user has paused typing for ≥ 200 ms. |
| **FR‑5** | Provide context‑aware suggestions (function names, variables, imports). | Suggestions are derived from the current file’s AST and imported modules. |
| **FR‑6** | Display suggestions in the VS Code completion UI. | Suggestions appear in the standard IntelliSense dropdown. |
| **FR‑7** | Allow user to configure the trigger delay. | A setting `lexiBoost.triggerDelay` (default 200 ms) is exposed in `settings.json`. |
| **FR‑8** | Persist user settings across sessions. | Settings are stored in VS Code’s global configuration. |
| **FR‑9** | Provide a “disable” toggle per language. | Settings `lexiBoost.enabledLanguages` allow disabling completions for any of the three languages. |
| **FR‑10** | Publish the extension to the VS Code Marketplace. | The `vsce` package is built and uploaded to the marketplace with proper metadata. |
| **FR‑11** | Log errors to the Output channel. | All errors are written to a dedicated `Lexi Boost` output channel. |
| **FR‑12** | Graceful fallback to VS Code’s default completions on failure. | If the provider throws, the extension does not block the default IntelliSense. |
| **FR‑13** | Support VS Code extensions API v1.70+. | The extension declares `engines.vscode` ≥ `1.70.0` in `package.json`. |
| **FR‑14** | Provide a README with installation and usage instructions. | The README contains installation steps, language support, and configuration examples. |
| **FR‑15** | Include unit tests for provider logic. | Tests cover AST parsing, suggestion generation, and delay logic. |
| **FR‑16** | Include integration tests that run in a headless VS Code instance. | Tests verify that suggestions appear after the configured delay. |

---

## 2. Non‑Functional Requirements

| Category | Requirement | Details |
|----------|-------------|---------|
| **Performance** | Latency | Completion suggestions must be generated and displayed within **100 ms** of the trigger after the 200 ms idle period. |
| | CPU | Provider logic should consume < 10 % CPU on a typical laptop during idle typing. |
| **Security** | Data Privacy | The extension must **not** send any user code or file contents to external services. |
| | Network | No outbound network traffic is allowed unless explicitly configured by the user. |
| | Permissions | Only `workspace` and `configuration` scopes are requested in `package.json`. |
| **Reliability** | Error Handling | All exceptions are caught; the extension logs to the Output channel and continues functioning. |
| | Recovery | If the provider fails, VS Code’s default completions remain available. |
| **Usability** | Configuration | Settings are exposed via VS Code’s Settings UI and can be edited in `settings.json`. |
| | Documentation | README and inline comments provide clear guidance. |
| **Maintainability** | Code Quality | TypeScript with strict compiler options (`noImplicitAny`, `strictNullChecks`). |
| | Testing | Minimum 80 % code coverage; CI pipeline runs tests on every push. |
| **Compatibility** | OS | Works on Windows, macOS, and Linux. |
| | VS Code | Supported on VS Code 1.70+ (including VS Code Insiders). |
| | Language Versions | Supports Python 3.6+, Go 1.13+, TypeScript 3.8+. |

---

## 3. Constraints

1. **Extension Size** – The final VSIX package must be ≤ 5 MB to ensure fast marketplace downloads.
2. **Dependencies** – Only official VS Code API and lightweight parsing libraries (e.g., `@typescript-eslint/typescript-estree`, `pyright` for Python) may be used. No heavy ML models or external services.
3. **Marketplace Policies** – Must comply with VS Code Marketplace terms: no hidden data collection, no malicious behavior.
4. **Build Process** – Must use `npm` scripts (`build`, `package`, `publish`) and `vsce` for packaging.
5. **License** – The extension must be released under an MIT‑style license (as per repository license).

---

## 4. Assumptions

- Users have a
