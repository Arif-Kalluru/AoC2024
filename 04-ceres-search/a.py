word1 = "XMAS"
word2 = word1[::-1]

lines = []
with open("input.txt", 'r') as f:
    for line in f:
        lines.append(line.rstrip())


def search(word: str) -> int:
    n = len(lines)
    m = len(lines[0])
    count = 0

    # search horizontal
    for line in lines:
        count += line.count(word)
    # search vertical
    for i in range(n - 3):
        for j in range(m):
            if (lines[i][j] == word[0] and lines[i+1][j] == word[1] and lines[i+2][j] == word[2] and lines[i+3][j] == word[3]):
                count += 1
    # search diagonal (right)
    for i in range(n - 3):
        for j in range(m - 3):
            if (lines[i][j] == word[0] and lines[i+1][j+1] == word[1] and lines[i+2][j+2] == word[2] and lines[i+3][j+3] == word[3]):
                count += 1
    # search diagonal (left)
    for i in range(n - 3):
        for j in range(3, m):
            if (lines[i][j] == word[0] and lines[i+1][j-1] == word[1] and lines[i+2][j-2] == word[2] and lines[i+3][j-3] == word[3]):
                count += 1

    return count

result = search(word1)
result += search(word2)
print(result)
