"""
  Kiran Ponappan Sreekumari 
  CSC505 – Principles of Software Development 
  Colorado State University - Global
  Dr. Pubali Banerjee 
  February 29, 2024
  Module 3: Critical Thinking
  Use Python to write a script that will print out the names and number of pages in your prototype and the sequence or flow of the pages. 
"""
import sys

def parse_sequence_diagram(uml_script):
    # Split the script by lines
    lines = uml_script.split('\n')

    # Initialize variables to store page names and flow
    page_names = []
    flow = []

    # Iterate through each line of the script
    for line in lines:
        # Remove leading and trailing whitespace
        line = line.strip()

        # Skip empty lines and comments
        if not line or line.startswith("'") or line.startswith('"'):
            continue

        # Extract page names
        if line.startswith('participant'):
            parts = line.split('"')
            if len(parts) > 1:
                page_name = parts[1]
                page_names.append(page_name)
       
        if '->' in line:
            flow.append(line)

    return page_names, flow

if __name__ == "__main__":
    # Check if the filename is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <uml_file>")
        sys.exit(1)

    filename = sys.argv[1]

    # Read the UML script from the file
    try:
        with open(filename, 'r') as file:
            uml_script = file.read()
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

    page_names, flow = parse_sequence_diagram(uml_script)

    print("Names of pages in prototype:")
    for name in page_names:
        print("-", name)

    print("\nSequence or flow of pages:")
    for step in flow:
        print(" ",step.replace("\\n",' '))