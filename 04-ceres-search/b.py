words = ["MAS", "SAM"]

lines = []
with open("input.txt", 'r') as f:
    for line in f:
        lines.append(line.rstrip())


def search() -> int:
    n = len(lines)
    m = len(lines[0])

    count = 0
    for i in range(n - 2):
        for j in range(m - 2):
            word1 = f"{lines[i][j]}{lines[i+1][j+1]}{lines[i+2][j+2]}"
            word2 = f"{lines[i+2][j]}{lines[i+1][j+1]}{lines[i][j+2]}"
            if word1 in words and word2 in words:
                count += 1
    return count

print(search())
