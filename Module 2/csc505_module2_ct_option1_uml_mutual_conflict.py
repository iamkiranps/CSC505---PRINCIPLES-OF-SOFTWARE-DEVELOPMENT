"""
  Kiran Ponappan Sreekumari 
  CSC505 – Principles of Software Development 
  Colorado State University - Global
  Dr. Pubali Banerjee 
  February 22, 2024
  Module 2: Critical Thinking - Option #1: Mutually Conflicting Requirements
  As a software developer seeking specifications from users, it is possible to encounter two stakeholders who have conflicting ideas about the specifications. 
  In particular, they may disagree on what the software should be. This phenomenon is known as "mutually conflicting requirements."
"""
import sys
import re

def extract_info(diagram_file):
    with open(diagram_file, 'r') as file:
        diagram_content = file.read()

    title_pattern = r'title (.*) '
    stakeholder_pattern = r'RECTANGLE (\w+) \{'
    communication_pattern = r' --> (\w+):'

    stakeholders = re.findall(stakeholder_pattern, diagram_content)
    communication_paths = re.findall(communication_pattern, diagram_content)
    pattern_name = re.findall(title_pattern, diagram_content)

    return pattern_name, stakeholders, len(communication_paths)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <diagram_file>")
        sys.exit(1)

    diagram_file = sys.argv[1]
    
    pattern_name, stakeholders, communication_pathways = extract_info(diagram_file)
    print()
    print("Name of the diagram:", pattern_name)
    print("Stakeholders:", stakeholders)
    print("Number of Communication Pathways:", communication_pathways)
    print()
    
if __name__ == "__main__":
    main()
