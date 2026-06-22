from lexi_boost import LexiBoost, Bug

def test_detect_bugs():
    lexi_boost = LexiBoost()
    code = 'let x = 5\nlet y = 10'
    bugs = lexi_boost.detect_bugs(code)
    assert len(bugs) == 2
    assert bugs[0].line == 1
    assert bugs[0].column == 9
    assert bugs[0].message == 'Missing semicolon'
    assert bugs[1].line == 2
    assert bugs[1].column == 10
    assert bugs[1].message == 'Missing semicolon'

def test_highlight_bugs():
    lexi_boost = LexiBoost()
    code = 'let x = 5\nlet y = 10'
    bugs = lexi_boost.detect_bugs(code)
    highlighted_code = lexi_boost.highlight_bugs(code, bugs)
    assert 'Missing semicolon' in highlighted_code

def test_get_tooltip():
    lexi_boost = LexiBoost()
    bug = Bug(1, 10, 'Missing semicolon')
    tooltip = lexi_boost.get_tooltip(bug)
    assert tooltip == 'Line 1, Column 10: Missing semicolon'

def test_detect_bugs_empty_code():
    lexi_boost = LexiBoost()
    code = ''
    bugs = lexi_boost.detect_bugs(code)
    assert len(bugs) == 0

def test_highlight_bugs_empty_code():
    lexi_boost = LexiBoost()
    code = ''
    bugs = lexi_boost.detect_bugs(code)
    highlighted_code = lexi_boost.highlight_bugs(code, bugs)
    assert highlighted_code == ''

def test_get_tooltip_none_bug():
    lexi_boost = LexiBoost()
    bug = None
    try:
        tooltip = lexi_boost.get_tooltip(bug)
        assert False, 'Expected AttributeError'
    except AttributeError:
        assert True
