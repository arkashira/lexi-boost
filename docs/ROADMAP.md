# Roadmap – lexi‑boost

> **Goal** – Deliver a lightweight, high‑quality VS Code extension that gives developers instant, inline code completions for Python, Go, and TypeScript.  
> **Scope** – The roadmap is split into three major phases:  
> 1. **MVP** – Minimum viable product that can be shipped to the marketplace.  
> 2. **v1** – Core feature expansion, performance tuning, and user‑experience polish.  
> 3. **v2** – AI‑driven completions, extensibility, and broader language support.

> **MVP‑critical items** are marked with **⚡**.  
> **Timeline** – Each phase is estimated in *sprint‑length* weeks (2‑week sprints).  

---

## Phase 0 – Pre‑MVP (Preparation)

| Sprint | Deliverable | Notes |
|--------|-------------|-------|
| 0.1 | Repo audit & CI setup | Ensure linting, tests, and CI are in place. |
| 0.2 | VS Code Extension skeleton | Use `yo code` to scaffold the extension. |
| 0.3 | Publish to Marketplace (beta) | Create a marketplace listing, set up billing, and gather early feedback. |

---

## Phase 1 – MVP (Must‑Have for Launch)

| Sprint | Deliverable | MVP‑critical? |
|--------|-------------|---------------|
| 1.1 | Register completion provider for Python, Go, TypeScript | ⚡ |
| 1.2 | Implement 200 ms debounce for suggestion trigger | ⚡ |
| 1.3 | Basic suggestion engine (static keyword list + simple context) | ⚡ |
| 1.4 | Basic UI – inline suggestion list with “Accept” and “Dismiss” actions | ⚡ |
| 1.5 | Unit & integration tests for provider logic | ⚡ |
| 1.6 | Packaging & publishing to VS Code Marketplace | ⚡ |
| 1.7 | Documentation (README, quick‑start, FAQ) |  |
| 1.8 | Basic telemetry (usage counts, error logs) |  |
| 1.9 | Release v0.1.0 |  |

### MVP Acceptance Criteria

1. **Functionality** – Users can type in a supported file and see inline suggestions after 200 ms.  
2. **Stability** – No crashes or memory leaks in typical usage.  
3. **Performance** – Latency < 50 ms for suggestion rendering.  
4. **Marketplace** – Extension is listed, installable, and passes Microsoft’s validation.  

---

## Phase 2 – v1 (Feature Expansion & Polish)

| Theme | Sprint | Deliverable |
|-------|--------|-------------|
| **Core Functionality** | 2.1 | Context‑aware suggestion ranking (simple heuristics: file scope, imports, cursor position). |
| | 2.2 | Support for additional file types (e.g., `.py`, `.go`, `.ts`, `.tsx`). |
| | 2.3 | Configurable debounce interval and suggestion limit via settings. |
| **Performance & UX** | 2.4 | Caching of recent completions to reduce recomputation. |
| | 2.5 | Asynchronous suggestion fetching to keep UI responsive. |
| | 2.6 | Keyboard shortcuts for navigating suggestions (Ctrl+Space, Tab). |
| **Extensibility** | 2.7 | Plugin API for third‑party providers (e.g., custom language models). |
| | 2.8 | Extension settings panel with live preview. |
| **Telemetry & Analytics** | 2.9 | Anonymous usage stats (suggestion acceptance rate, error rates). |
| | 2.10 | Error reporting to a lightweight backend (Sentry). |
| **Documentation & Community** | 2.11 | Comprehensive docs, contribution guide, and issue templates. |
| | 2.12 | Release v1.0.0 |  

### v1 Acceptance Criteria

- **Feature completeness** – All themes above are implemented and documented.  
- **User satisfaction** – Early beta users report >80 % acceptance of suggestions.  
- **Stability** – No critical bugs in 90 % of test cases.  
- **Performance** – Average suggestion latency < 30 ms under typical load.  

---

## Phase 3 – v2 (AI‑Driven, Multi‑Language, Community‑Powered)

| Theme | Sprint | Deliverable |
|-------|--------|-------------|
| **AI Integration** | 3.1 | Plug‑in for local LLM inference (e.g., vLLM) with minimal model size. |
| | 3.2 | Fine‑tuning support for user‑provided datasets (Python, Go, TS). |
| | 3.3 | Context‑aware code generation (full line/statement suggestions). |
| **Language Expansion** | 3.4 | Add support for Rust, Java, and C# with language‑specific heuristics.
