import pytest
from pathlib import Path
from lexi_boost import parse_source, generate_markdown, process_directory, FunctionDoc


def test_parse_source_basic_function():
    """Test parsing a simple public function."""
    source = """
def add(a, b):
    '''Adds two numbers.'''
    return a + b
"""
    result = parse_source(source)
    assert len(result) == 1
    assert result[0].name == "add"
    assert "def add(a, b):" in result[0].signature
    assert result[0].docstring == "Adds two numbers."


def test_parse_source_private_function_ignored():
    """Test that private functions (starting with _) are ignored."""
    source = """
def public_func():
    pass

def _private_func():
    pass
"""
    result = parse_source(source)
    assert len(result) == 1
    assert result[0].name == "public_func"


def test_parse_source_syntax_error():
    """Test that files with syntax errors return an empty list."""
    source = "def broken(("
    result = parse_source(source)
    assert result == []


def test_parse_source_no_docstring():
    """Test functions without docstrings."""
    source = "def simple(): pass"
    result = parse_source(source)
    assert len(result) == 1
    assert result[0].docstring is None


def test_generate_markdown_content():
    """Test the markdown generation logic."""
    funcs = [
        FunctionDoc(
            name="calculate",
            signature="def calculate(x, y=10):",
            docstring="Performs a calculation."
        )
    ]
    md = generate_markdown("math.utils", funcs)
    
    assert "# Documentation for `math.utils`" in md
    assert "## `calculate`" in md
    assert "### Signature" in md
    assert "def calculate(x, y=10):" in md
    assert "Performs a calculation." in md


def test_generate_markdown_empty_list():
    """Test markdown generation when no functions are found."""
    md = generate_markdown("empty.module", [])
    assert "No public functions found" in md


def test_process_directory_integration(tmp_path: Path):
    """Test the full end-to-end directory processing."""
    # Setup source directory structure
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    
    # Create a dummy python file
    (src_dir / "core.py").write_text("""
def greet(name):
    '''Greets the user.'''
    return f"Hello {name}"

def _secret():
    pass
""")

    # Create a subdirectory with another file
    sub_dir = src_dir / "utils"
    sub_dir.mkdir()
    (sub_dir / "helper.py").write_text("""
def help_me():
    '''Provides help.'''
    pass
""")

    # Define output directory
    docs_dir = tmp_path / "docs"

    # Run the processor
    process_directory(src_dir, docs_dir)

    # Verify output files exist
    assert (docs_dir / "core.md").exists()
    assert (docs_dir / "utils" / "helper.md").exists()

    # Verify content of core.md
    core_content = (docs_dir / "core.md").read_text()
    assert "## `greet`" in core_content
    assert "Greets the user." in core_content
    assert "_secret" not in core_content  # Private functions should not appear

    # Verify content of helper.md
    helper_content = (docs_dir / "utils" / "helper.md").read_text()
    assert "## `help_me`" in helper_content
    assert "Provides help." in helper_content


def test_process_directory_invalid_source(tmp_path: Path):
    """Test that process_directory raises ValueError for non-existent source."""
    with pytest.raises(ValueError, match="does not exist"):
        process_directory(tmp_path / "nonexistent", tmp_path / "docs")
