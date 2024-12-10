def read_grid(filename):
    with open(filename) as file:
        return [line.rstrip() for line in file]


def collect_antennas(grid):
    antennas = {}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != '.':
                antennas.setdefault(cell, []).append((i, j))
    return antennas


def calculate_antinodes(grid, antennas):
    antinodes = set()
    n, m = len(grid), len(grid[0])

    for positions in antennas.values():
        k = len(positions)
        for i in range(k - 1):
            for j in range(i + 1, k):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                x_diff, y_diff = x1 - x2, y1 - y2

                antinodes.update([(x1, y1), (x2, y2)]) # current antennas also count as antinode positions

                # Add antinodes extending along the line
                antinodes.update(extend_antinodes(x1, y1, x_diff, y_diff, n, m))
                antinodes.update(extend_antinodes(x2, y2, -x_diff, -y_diff, n, m))

    return antinodes


def extend_antinodes(x, y, x_diff, y_diff, n, m):
    result = set()
    while 0 <= x + x_diff < n and 0 <= y + y_diff < m:
        x += x_diff
        y += y_diff
        result.add((x, y))
    return result


def main():
    grid = read_grid("input.txt")
    antennas = collect_antennas(grid)
    antinodes = calculate_antinodes(grid, antennas)
    print(len(antinodes))


if __name__ == '__main__':
    main()