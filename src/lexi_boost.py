import ast
import os
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass
class FunctionDoc:
    """Data class representing a function's documentation."""
    name: str
    signature: str
    docstring: Optional[str]


def parse_source(source_code: str) -> List[FunctionDoc]:
    """
    Parses Python source code and extracts documentation for public functions.

    Args:
        source_code: A string containing the Python source code.

    Returns:
        A list of FunctionDoc objects for public functions (not starting with _).
    """
    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        # If the file has syntax errors, we skip it gracefully.
        return []

    docs: List[FunctionDoc] = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and not node.name.startswith('_'):
            # ast.unparse is available in Python 3.9+
            # It reconstructs the source code from the AST node.
            signature = ast.unparse(node)
            docstring = ast.get_docstring(node)
            docs.append(FunctionDoc(
                name=node.name,
                signature=signature,
                docstring=docstring
            ))
    return docs


def generate_markdown(module_name: str, functions: List[FunctionDoc]) -> str:
    """
    Generates a Markdown string from a list of FunctionDoc objects.

    Args:
        module_name: The name of the module (e.g., 'src.utils').
        functions: A list of FunctionDoc objects.

    Returns:
        A formatted Markdown string.
    """
    lines = [f"# Documentation for `{module_name}`\n\n"]

    if not functions:
        lines.append("*No public functions found in this module.*\n")
        return "".join(lines)

    for func in functions:
        lines.append(f"## `{func.name}`\n\n")
        lines.append("### Signature\n\n")
        lines.append("```python\n")
        lines.append(f"{func.signature}\n")
        lines.append("```\n\n")

        lines.append("### Description\n\n")
        if func.docstring:
            lines.append(f"{func.docstring}\n\n")
        else:
            lines.append("*No description provided.*\n\n")

        lines.append("---\n\n")

    return "".join(lines)


def process_directory(source_root: Path, output_root: Path) -> None:
    """
    Walks through a source directory, generates docs for .py files,
    and writes them to the output directory mirroring the structure.

    Args:
        source_root: The root directory of the source code.
        output_root: The directory where markdown docs will be saved.
    """
    if not source_root.is_dir():
        raise ValueError(f"Source directory '{source_root}' does not exist or is not a directory.")

    # Ensure output directory exists
    output_root.mkdir(parents=True, exist_ok=True)

    for py_file in source_root.rglob("*.py"):
        # Calculate relative path to maintain structure
        relative_path = py_file.relative_to(source_root)
        
        # Read source
        try:
            source_content = py_file.read_text()
        except (IOError, OSError):
            # Skip files that cannot be read
            continue

        # Extract documentation
        functions = parse_source(source_content)

        # Create module name (e.g., src/module -> src.module)
        module_name = str(relative_path.with_suffix("")).replace(os.sep, ".")

        # Generate markdown
        md_content = generate_markdown(module_name, functions)

        # Determine output file path (e.g., docs/module.md)
        output_file = output_root / relative_path.with_suffix(".md")
        
        # Ensure parent directories exist in output
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Write documentation
        output_file.write_text(md_content)
