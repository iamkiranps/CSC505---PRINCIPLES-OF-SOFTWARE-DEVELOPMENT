"""
  Kiran Ponappan Sreekumari 
  CSC505 – Principles of Software Development 
  Colorado State University - Global
  Dr. Pubali Banerjee 
  March 14, 2024
  Module 4: Critical Thinking - Web-based Pothole Tracking and Repair System
  Use Python to write a script that will print out the different actors and use cases and a brief description of your diagram.
 """
import sys
def parse_use_cases(uml_script):
    use_cases = {}
    current_use_case = None
    in_use_case = False      
    for line in uml_script.split('\n'):
        if 'usecase' in line:
            use_case_name = line.split('"')[1]
            current_use_case = use_case_name
            use_cases[current_use_case] = []
            in_use_case = True
        elif in_use_case and (not line.strip().startswith('/') and \
                              not line.strip().endswith('/') and \
                                not line.endswith('}') and not '-->' in line ):
            description = line.strip()
            use_cases[current_use_case].append(description)
        elif '->' in line:
            in_use_case = False

    return use_cases

def parse_actors(uml_script):
    actors = []
    for line in uml_script.split('\n'):
        if 'actor' in line:
            actor_name = line.split('"')[1]
            actors.append(actor_name)
        elif 'rectangle' in line:
            break
    return actors

def main(uml_file_path):
    with open(uml_file_path, 'r') as file:
        uml_script = file.read()

    actors = parse_actors(uml_script)
    use_cases = parse_use_cases(uml_script)

    print("Actors:")
    for actor in actors:
        print("-", actor)

    print("\nUse Cases:")

    for use_case, descriptions in use_cases.items():
        print("-", use_case)
        print("  Description:")
        for description in descriptions:
            print("    -", description)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <uml_file>")
        sys.exit(1)
    uml_file = sys.argv[1]
    main(uml_file)
