import ast
import re


class PlantUMLGenerator:
    def __init__(self, python_file):
        self.python_file = python_file  
        self.class_names = []
        self.functions = []
    
    def generate(self):
        with open(self.python_file, 'r') as f:
            self.tree = ast.parse(f.read())
            self.visit_tree(self.tree)
        
        print("@startuml")
                
        for c in self.class_names:
            print(f"class {c} {{")
            
            for f in self.functions:
                if f.startswith(c):
                    print(f"\t+ {f[len(c)+1:]}()")
                    
            print("}")
        
        print("@enduml") 
        
    def visit_tree(self, node):
        if isinstance(node, ast.ClassDef):
            self.class_names.append(node.name) 
        
        if isinstance(node, ast.FunctionDef):
            self.functions.append(node.name)
 
        for child in ast.iter_child_nodes(node):
            self.visit_tree(child)
            
generator = PlantUMLGenerator('mycode.py')
generator.generate()
