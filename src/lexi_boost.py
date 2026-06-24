import argparse
import json
from dataclasses import dataclass

@dataclass
class CompilationStatus:
    success: bool
    message: str

def compile_code(file_path: str) -> CompilationStatus:
    try:
        with open(file_path, 'r') as file:
            code = file.read()
        # Simulate compilation by checking for syntax errors
        try:
            compile(code, file_path, 'exec')
            return CompilationStatus(True, 'Compilation successful')
        except SyntaxError:
            return CompilationStatus(False, 'Compilation failed')
    except FileNotFoundError:
        return CompilationStatus(False, 'File not found')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='Path to the code file')
    args = parser.parse_args()
    status = compile_code(args.file_path)
    print(json.dumps(status.__dict__))

if __name__ == '__main__':
    main()
