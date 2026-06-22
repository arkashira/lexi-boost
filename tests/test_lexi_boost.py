from lexi_boost import LexiBoost, CodeSnippet

def test_add_code_snippet():
    lexi_boost = LexiBoost()
    lexi_boost.add_code_snippet("Python", "print('Hello World')")
    assert len(lexi_boost.get_code_snippets()) == 1

def test_get_code_snippets():
    lexi_boost = LexiBoost()
    lexi_boost.add_code_snippet("Python", "print('Hello World')")
    lexi_boost.add_code_snippet("Go", "fmt.Println('Hello World')")
    assert len(lexi_boost.get_code_snippets("Python")) == 1
    assert len(lexi_boost.get_code_snippets("Go")) == 1

def test_generate_documentation():
    lexi_boost = LexiBoost()
    lexi_boost.add_code_snippet("Python", "print('Hello World')")
    documentation = lexi_boost.generate_documentation("Python")
    assert "### Python" in documentation
    assert "print('Hello World')" in documentation

def test_detect_bugs():
    lexi_boost = LexiBoost()
    code = "print('Hello World'"
    assert "Bug detected: syntax error" in lexi_boost.detect_bugs(code)
    code = "print('Hello World')"
    assert "No bugs detected" in lexi_boost.detect_bugs(code)

def test_complete_code():
    lexi_boost = LexiBoost()
    code = "print('Hello World')"
    completed_code = lexi_boost.complete_code(code, "Python")
    assert "print('Completed code in Python')" in completed_code
