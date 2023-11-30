import ast

py_file = "mycode.py"  

classes = []
methods = [] 
current_class = None

with open(py_file) as f:
    tree = ast.parse(f.read())
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            current_class = node.name 
            classes.append(current_class)
            
        elif isinstance(node, ast.FunctionDef):
            methods.append(f"{current_class}.{node.name}")
            
print(f"// Parsed from {py_file}")
print("@startuml") 

# Print plantuml diagram

print("@enduml")
