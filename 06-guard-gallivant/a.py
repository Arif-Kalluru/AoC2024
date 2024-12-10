grid = []
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # ^, >, v, <

def main():
    guards = "^>v<" # corresponds to dirs
    start_r = 0
    start_c = 0
    start_dir = 0 # index into dirs
    found_start = False

    with open("input.txt", "r") as file:
        r = 0
        for line in file:
            grid.append(list(line))
            if found_start:
                continue
            for i in range(len(guards)):
                guard = guards[i]
                if guard in line:
                    start_r = r
                    start_c = line.find(guard)
                    start_dir = i
                    found_start = True
                    break
            r += 1
    
    curr_dir, r, c = start_dir, start_r, start_c
    n, m = len(grid), len(grid[0])
    path = set() # all coordinates traversed by the guard

    while True:
        path.add((r, c))
        nr, nc = r + dirs[curr_dir][0], c + dirs[curr_dir][1]
        if nr not in range(n) or nc not in range(m): # Out of bounds
            break
        if grid[nr][nc] == '#':
            curr_dir = (curr_dir + 1) % 4
        else:
            r, c = nr, nc
    
    print(len(path))

if __name__ == '__main__':
    main()