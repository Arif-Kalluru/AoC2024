# - Graph, number of incoming edges is inversely proportional to it's order
# - Can't do a complete list using the all the rules because the rules can be/are cyclic in nature
# - Ordered list with the required rules for individual lists can be made because they are not/shouldn't be cyclic

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

def order_list(nums):
    # Create order using the subset of rules needed
    order = {} # number and it's order

    for rule in rules:
        rule = rule.split("|")
        if rule[0] not in nums or rule[1] not in nums: # we don't care about this rule
            continue
        if rule[0] not in order: # LHS not in map
            order[rule[0]] = 0
        if rule[1] not in order: # RHS not in map
            order[rule[1]] = 0
        order[rule[1]] += 1
    
    # Put number in it's correct order
    n = len(order) 
    nums = [0] * n
    for num in order:
        nums[order[num]] = num
    return nums

result = 0

for i in range(len(updates)):
    n = len(updates[i])
    invalid = False
    for j in range(n-1):
        order = f"{updates[i][j]}|{updates[i][j+1]}"
        if order not in rules:
            invalid = True
            break
    if invalid: # add only for invalid lists
        ordered_update = order_list(updates[i])
        result += int(ordered_update[n//2])

print(result)