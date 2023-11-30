import ast
import textwrap

def generate_diagram(py_file):
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
       
    print(f"// Generated from {py_file}")
    
    print("@startuml")
    
    wrapper = textwrap.TextWrapper(initial_indent='\t',  
                                   subsequent_indent='\t')
                                   
    for c in classes:
        print(f"class {c} {{")
        
        class_methods = [m.split('.')[-1] for m in methods if c in m]  
        printed_methods = wrapper.fill(" ".join(class_methods))
        print(printed_methods)

        print("}\n")

    print("@enduml")

    
generate_diagram("mycode.py")
