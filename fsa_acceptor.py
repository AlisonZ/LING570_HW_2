import re

RESULTS = {}
FSA = {}
START_STATE = ''
FINAL_STATE = ''

def createFSA(rule):
    clean_rule = re.sub(r"\(|\)|\"|\"", "", rule)
    split_rule = clean_rule.split()
    initial_state = split_rule[0]
    next_state = split_rule[1]
    unit = split_rule[2]

    if initial_state in FSA.keys():
        existing_state = FSA[initial_state]
        if next_state in existing_state.keys():
            existing_units = existing_state.values()
            if unit not in existing_units:
                unit_list = list(existing_units)
                FSA[initial_state].update({next_state: unit_list})
                unit_list.append(unit)
        else:
            FSA[initial_state].update({next_state: unit})
    else:
        FSA[initial_state] = {next_state: unit}

def read_fsa_rules(fsa_rules):
    with open(fsa_rules, 'r', encoding='utf8') as file:
        rules = file.readlines()
        global FINAL_STATE, START_STATE
        FINAL_STATE = rules.pop(0).strip()
        START_STATE = rules[0].split("(")[1].strip()
        for rule in rules:
            createFSA(rule.strip())
        

# READ IN THE STRING
# Easy outs
# Check that all chars in the string are permissible in the FSA
# Check that initial char is a permissible q0
# Check that final char is permissibile qfinal

def find_matching_states(char, valid_movements):
    valid_next_states = []
    for key, values in valid_movements.items():
        if char in values:
            valid_next_states.append(key)
    return valid_next_states

def validate_input(input, current_state):
    valid_movements = FSA[current_state]
    accepted_inputs = list(valid_movements.values())
    flattened_list = [item for sublist in accepted_inputs for item in sublist]
    for char in input:
        if char in flattened_list:
            next_state = find_matching_states(char, valid_movements)
    #         # TODO: update to handle multiple valid next states
            return validate_input(input[1:], next_state[0])
        else:
            return False
    
    return current_state == FINAL_STATE

def read_input(input_file):
     with open(input_file, 'r', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            stripped_line = line.strip()
            clean_line = re.sub(r"\"|\"", "", stripped_line)
            input_array = clean_line.split(" ")
            isValidInput = validate_input(input_array, START_STATE)
            RESULTS[stripped_line] =  "yes" if isValidInput else "no"

def print_results():
    for key, value in RESULTS.items():
        print(f"{key} => {value}")

def main():

    fsa_definition = './fsa_1.txt'
    input_file = "./ex.txt"
    read_fsa_rules(fsa_definition)
    read_input(input_file)
    print_results()
main()