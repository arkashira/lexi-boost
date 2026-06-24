# Lexi-Boost

Lexi-Boost is a lightweight, standard-library-only Python tool that automatically generates Markdown documentation for your codebase. It scans your source directory, identifies public functions, and creates structured documentation files including signatures and docstrings.

## Features

- **Zero Dependencies**: Runs on Python 3.9+ standard library only.
- **Automatic Scanning**: Recursively finds `.py` files in your source directory.
- **Public API Focus**: Only documents public functions (those not starting with `_`).
- **Markdown Output**: Generates clean, readable Markdown files mirroring your source structure.

## Installation

No external packages required. Just ensure you have Python 3.9 or higher.

## Usage

You can use Lexi-Boost as a module or integrate it into your CI/CD pipeline.

### Command Line
