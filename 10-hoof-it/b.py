def solve(x, y, n, m, topograph, memo):
    if memo[x][y] is not None: # Return cached result
        return memo[x][y]

    if topograph[x][y] == 9: # Endpoint
        return 1

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
    memo[x][y] = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and topograph[nx][ny] == topograph[x][y] + 1:
            memo[x][y] += solve(nx, ny, n, m, topograph, memo)
    
    return memo[x][y]

def main():
    topograph = []
    zeros = []

    with open("input.txt", "r") as file:
        for i, line in enumerate(file):
            row = list(map(int, line.strip()))
            topograph.append(row)
            zeros.extend((i, j) for j, num in enumerate(row) if num == 0)
    
    n, m = len(topograph), len(topograph[0])
    memo = [[None for _ in range(m)] for _ in range(n)] # memoization table
    total_count = 0

    for x, y in zeros:
        total_count += solve(x, y, n, m, topograph, memo)
    
    print(total_count)

if __name__ == '__main__':
    main()