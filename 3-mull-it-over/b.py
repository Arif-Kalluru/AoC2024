import re

do_str = "do()"
dont_str = "don't()"

with open('input.txt', 'r') as f:
    content = f.read()

content = content.split(dont_str)
valid = []
valid.append(content[0]) # portion before first don't is always valid
content = content[1:]

for str in content:
    if do_str not in str: # if not do string, then it's invalid
        continue
    instrs = str.split(do_str) 
    instrs = instrs[1:] # portion in between don't and do is invalid, so remove it
    for instr in instrs:
        valid.append(instr)

# Regex pattern to match mul(...) and extract the digits
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

result = 0

for instr in valid:
    matches = re.findall(pattern, instr)
    for match in matches:
        first_num, second_num = map(int, match)
        result += first_num * second_num

print(result)
