import ast

def check_docstrings(filename):
    with open(filename, "r") as file:
        tree = ast.parse(file.read())

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)) and not ast.get_docstring(node):
            print(f"Missing docstring for: {node.name}")

# Specify the Python file you want to check
filename = "square.py"
check_docstrings(filename)
