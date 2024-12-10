# O(n) memory, O(n+m) time

updates = []
rules = set()

with open("input.txt", "r") as f:
    rules_input = True
    for line in f:
        line = line.rstrip()
        if line == '':
            rules_input = False
            continue
        if rules_input: # parsing input with rules
            rules.add(line)
        else: # parsing input with updates
            line = line.split(',')
            updates.append(line)

result = 0

for i in range(len(updates)):
    n = len(updates[i])
    valid = True
    for j in range(n-1):
        order = f"{updates[i][j]}|{updates[i][j+1]}"
        if order not in rules: 
            valid = False
            break
    if valid:
        result += int(updates[i][n//2])

print(result)