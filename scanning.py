import ast
import re


class PlantUMLGenerator:
    def __init__(self, python_file):
        self.python_file = python_file
        self.class_names = []
        self.associations = []
    
    def generate(self):
        with open(self.python_file, 'r') as f:
            self.tree = ast.parse(f.read())
            self.visit_tree(self.tree)
        
        plantuml_text ="@startuml\n"
        
        for m in self.associations:
            src, dst = m
            plantuml_text += f"{src} ..> {dst}\n"
        
        for c in self.class_names:
            plantuml_text += f"class {c} {{\n"
            
            # You can populate methods here e.g.
            # plantuml_text += f"\t+ {method_name}()\n" 
            
            plantuml_text += "}\n"
            
        plantuml_text += "@enduml"
        print(plantuml_text)
        
    def visit_tree(self, node):
        if isinstance(node, ast.ClassDef):
            self.class_names.append(node.name)
        
        if isinstance(node, ast.FunctionDef):
            # Can gather method names here
            
            pass # Remove this when gathering methods
        
        for child in ast.iter_child_nodes(node):  
            if isinstance(child, ast.ClassDef):
                self.visit_tree(child)

if __name__ == "__main__":
    gen = PlantUMLGenerator('my_code.py')
    gen.generate()
