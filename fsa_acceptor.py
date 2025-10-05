import re

FSA ={}
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

def read_input(input_text):
    with open(input_text, 'r', encoding='utf8') as file:
        rules = file.readlines()
        global FINAL_STATE, START_STATE
        FINAL_STATE = rules.pop(0)
        START_STATE = rules[0].split("(")[1]
        for rule in rules:
            createFSA(rule.strip())
        

# READ IN THE STRING
# Easy outs
# Check that all chars in the string are permissible in the FSA
# Check that initial char is a permissible q0
# Check that final char is permissibile qfinal
def validate_input(input):
   FSA
   for char in input:
       print(char)

# WITH FSA
# start with setting the node
# get first char
# see if the initial node has an endpoints that take the char
# if so, update the node to that node and get next char


# "a" "a" "b" --> False

def main():
    fsa_definition = './dfa1.txt'
    input = "a" "a" "b"
    read_input(fsa_definition)
    validate_input(input)
    print("!!!", START_STATE)


main()