import re

with open('input.txt', 'r') as f:
    content = f.read()


# Regex pattern to match mul(...) and extract the digits
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, content)
print(matches)

result = 0

for match in matches:
    first_num, second_num = map(int, match)
    result += first_num * second_num

print(result)
