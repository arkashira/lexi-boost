from lexi_boost import LexiBoost, CompletionItem

def test_get_completion_items():
    lexi_boost = LexiBoost()
    completion_items = lexi_boost.get_completion_items("python")
    assert len(completion_items) == 1
    assert completion_items[0].label == "print"

def test_register_completion_provider():
    lexi_boost = LexiBoost()
    result = lexi_boost.register_completion_provider("python")
    assert result == "Registered completion provider for python"

def test_register_completion_provider_unsupported_language():
    lexi_boost = LexiBoost()
    try:
        lexi_boost.register_completion_provider("java")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Unsupported language: java"

def test_get_completion_suggestions():
    lexi_boost = LexiBoost()
    completion_items = lexi_boost.get_completion_suggestions("python", "pr")
    assert len(completion_items) == 1
    assert completion_items[0].label == "print"

def test_get_completion_suggestions_empty_prefix():
    lexi_boost = LexiBoost()
    completion_items = lexi_boost.get_completion_suggestions("python", "")
    assert len(completion_items) == 1
    assert completion_items[0].label == "print"

def test_get_completion_suggestions_no_match():
    lexi_boost = LexiBoost()
    completion_items = lexi_boost.get_completion_suggestions("python", "xyz")
    assert len(completion_items) == 0
