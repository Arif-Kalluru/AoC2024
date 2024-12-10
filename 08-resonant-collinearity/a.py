antennas = {}
grid = []

def main():
    with open("input.txt") as file:
        for line in file:
            grid.append(line.rstrip())

    n, m = len(grid), len(grid[0])
    
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != '.':
                antennas.setdefault(cell, []).append((i, j))
    
    antinodes = set()

    for positions in antennas.values():
        k = len(positions)
        for i in range(k-1):
            for j in range(i+1, k):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                x_diff, y_diff = x1 - x2, y1 - y2
                anode1, anode2 = (x1 + x_diff, y1 + y_diff), (x2 - x_diff, y2 - y_diff)
                if 0 <= anode1[0] < n and 0 <= anode1[1] < m:
                    antinodes.add(anode1)
                if 0 <= anode2[0] < n and 0 <= anode2[1] < m:
                    antinodes.add(anode2)
    
    print(len(antinodes))

if __name__ == '__main__':
    main()