import json
import sys
import io
import argparse
from contextlib import redirect_stdout
from unittest.mock import patch
from src.lexi_boost import compile_code, CompilationStatus

def test_compile_code_success():
    with open('test_code.py', 'w') as file:
        file.write('print("Hello World")')
    status = compile_code('test_code.py')
    assert status.success
    assert status.message == 'Compilation successful'

def test_compile_code_failure():
    with open('test_code.py', 'w') as file:
        file.write('print("Hello World"')
    status = compile_code('test_code.py')
    assert not status.success
    assert status.message == 'Compilation failed'

def test_compile_code_file_not_found():
    status = compile_code('non_existent_file.py')
    assert not status.success
    assert status.message == 'File not found'

def test_main():
    with open('test_code.py', 'w') as file:
        file.write('print("Hello World")')
    with patch.object(sys, 'argv', ['lexi-boost', 'test_code.py']):
        with redirect_stdout(io.StringIO()) as f:
            from src.lexi_boost import main
            main()
    output = f.getvalue()
    status = json.loads(output)
    assert status['success']
    assert status['message'] == 'Compilation successful'
