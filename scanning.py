import re

class_pattern = r"class (\w+):"
function_pattern = r"def (\w+)\("

with open('mycode.py') as f:
    contents = f.read()

classes = re.findall(class_pattern, contents)
functions = re.findall(function_pattern, contents)

print("@startuml")
for c in classes:
    print(f"class {c} {{")
    matched_functions = [f for f in functions if f.startswith(c+"_")] 
    for f in matched_functions:
        print(f"\t+ {f[len(c)+1:]}()") 
    print("}\n")
print("@enduml")
