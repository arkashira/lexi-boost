import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lexi_boost import generate_code, check_dependencies, check_api_signatures, check_static_type, LLMConfig, Dependency
import pytest

def test_generate_code():
    llm_config = LLMConfig([Dependency("math", "1.0")])
    prompt = "print(math.pi)"
    code = generate_code(llm_config, prompt)
    assert code == "import math\nprint(math.pi)\n"

def test_check_dependencies():
    code = "import math\nprint(math.pi)"
    dependencies = [Dependency("math", "1.0")]
    assert check_dependencies(code, dependencies)

def test_check_dependencies_failure():
    code = "import math\nprint(math.pi)"
    dependencies = [Dependency("random", "1.0")]
    assert not check_dependencies(code, dependencies)

def test_check_api_signatures():
    code = "import math\nprint(math.pi)"
    dependencies = [Dependency("math", "1.0")]
    assert check_api_signatures(code, dependencies)

def test_check_api_signatures_failure():
    code = "import math\nprint(pi)"
    dependencies = [Dependency("math", "1.0")]
    assert not check_api_signatures(code, dependencies)

def test_check_static_type():
    code = "import math\nprint(math.pi)"
    assert check_static_type(code)

def test_check_static_type_failure():
    code = "import math\nprint(math."
    assert not check_static_type(code)
