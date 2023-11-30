import ast
import textwrap

py_file = "mycode.py"

classes = []  
methods = []

with open(py_file) as f:
    tree = ast.parse(f.read())
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, ast.FunctionDef): 
            methods.append(f"{node.parent.name}.{node.name}")
            
print(f"// Parsed from {py_file}")                
print("@startuml")

# Print class diagram like previous example 

print("@enduml")
