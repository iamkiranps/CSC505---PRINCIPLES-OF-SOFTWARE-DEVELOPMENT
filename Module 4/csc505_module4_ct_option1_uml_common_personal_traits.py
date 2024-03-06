"""
  Kiran Ponappan Sreekumari 
  CSC505 – Principles of Software Development 
  Colorado State University - Global
  Dr. Pubali Banerjee 
  March 6, 2024
  Module 4: Critical Thinking
  Using your personal experience and observation of people who are excellent software developers, 
  use a UML diagram of your choice to depict three personality traits that appear to be common among them. 
  Write a Python Script that will print  a brief description and names and number of the important steps in your program.
"""
import sys
import re

def extract_attributes_from_class(class_text):
    attributes = {}
    lines = class_text.split('\n')
    for line in lines:
        match = re.match(r'\s*- (\w+): (\w+)\s*/\'(.*)\'/', line.strip())
        if match:
            attribute_name = match.group(1)
            attribute_type = match.group(2)
            attribute_description = match.group(3)
            attributes[attribute_name] = {'type': attribute_type, 'description': attribute_description}
    return attributes

def main(uml_file):
    with open(uml_file, 'r') as file:
        uml_content = file.read()

    classes = re.findall(r'class (\w+) {([\s\S]*?)}', uml_content)

    for class_name, class_text in classes:
        print(f"Class: {class_name}")
        attributes = extract_attributes_from_class(class_text)
        for attribute_name, attribute_info in attributes.items():
            print(f"  {attribute_name} : {attribute_info['description']}")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <uml_file>")
        sys.exit(1)
    uml_file = sys.argv[1]
    main(uml_file)
