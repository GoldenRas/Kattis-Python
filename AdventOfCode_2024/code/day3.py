import re

def parse_instructions(input_text):
    # Regular expression to find valid mul instructions
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    # Regular expression to find do and don't instructions
    control_pattern = re.compile(r'do\(\)|don\'t\(\)')
    
    instructions = []
    for match in mul_pattern.finditer(input_text):
        instructions.append(('mul', int(match.group(1)), int(match.group(2)), match.start()))
    
    for match in control_pattern.finditer(input_text):
        instructions.append((match.group(0), match.start()))
    
    # Sort instructions by their position in the input text
    instructions.sort(key=lambda x: x[-1])
    
    return instructions

def process_instructions(instructions):
    enabled = True
    total = 0
    
    for instruction in instructions:
        if instruction[0] == 'do()':
            enabled = True
        elif instruction[0] == 'don\'t()':
            enabled = False
        elif instruction[0] == 'mul' and enabled:
            total += instruction[1] * instruction[2]
    
    return total

def main():
    with open('input/day3.txt', 'r') as file:
        input_text = file.read()
    
    instructions = parse_instructions(input_text)
    result = process_instructions(instructions)
    
    print(result)

if __name__ == "__main__":
    main()