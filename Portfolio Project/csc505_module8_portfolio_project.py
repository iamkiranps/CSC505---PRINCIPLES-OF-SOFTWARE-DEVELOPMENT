"""
  Kiran Ponappan Sreekumari 
  CSC505 – Principles of Software Development 
  Colorado State University - Global
  Dr. Pubali Banerjee 
  April 2, 2024
  Module 8: Portfolio Project
  Write a Python Script that will print all the steps in sequence for all the operations at the teller machine as shown in your diagram(s)
 """
import re
import sys

def extract_steps_from_uml_file(uml_file):
    steps = []
    with open(uml_file, 'r') as file:
        for line in file:
            match = re.search(r'/\'(.*?)\'/', line)
            if match:
                steps.append(match.group(1))
    return steps

def print_sequence_steps(steps):
    counter = 1
    for step in steps:
        if step.startswith('*'):
            print(f'{counter}.{step.replace("*","")}')
            counter+=1
        else:
            print(f'  {step}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <uml_file>")
        sys.exit(1)
    
    uml_file = sys.argv[1]
    steps = extract_steps_from_uml_file(uml_file)
    print("\n")
    print_sequence_steps(steps)
    print("\n")
