from lexi_boost import LexiBoost, CodeSnippet
import json
import os
import pytest

@pytest.fixture
def repo_path(tmp_path):
    # Create a temporary repository path
    return tmp_path / "repo"

@pytest.fixture
def api_specs_path(tmp_path):
    # Create a temporary API specs path
    api_specs = {"openapi": "3.0.0", "info": {"title": "API", "version": "1.0.0"}}
    api_specs_path = tmp_path / "api_specs.json"
    with open(api_specs_path, "w") as f:
        json.dump(api_specs, f)
    return api_specs_path

def test_lexi_boost_init(repo_path, api_specs_path):
    lexi_boost = LexiBoost(repo_path, api_specs_path)
    assert lexi_boost.repo_path == repo_path
    assert lexi_boost.api_specs_path == api_specs_path

def test_lexi_boost_train_model(repo_path, api_specs_path):
    lexi_boost = LexiBoost(repo_path, api_specs_path)
    trained_model = lexi_boost.train_model()
    assert isinstance(trained_model, CodeSnippet)
    assert trained_model.syntax_accuracy == 0.95

def test_lexi_boost_generate_code_snippet(repo_path, api_specs_path):
    lexi_boost = LexiBoost(repo_path, api_specs_path)
    code_snippet = lexi_boost.generate_code_snippet()
    assert code_snippet == "print('Hello World')"

def test_lexi_boost_invalid_api_specs_path(repo_path):
    invalid_api_specs_path = "invalid_path"
    with pytest.raises(FileNotFoundError):
        LexiBoost(repo_path, invalid_api_specs_path)

def test_lexi_boost_invalid_repo_path(api_specs_path):
    invalid_repo_path = "invalid_path"
    lexi_boost = LexiBoost(invalid_repo_path, api_specs_path)
    assert lexi_boost.repo_path == invalid_repo_path
