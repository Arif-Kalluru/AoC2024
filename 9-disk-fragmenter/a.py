def main():
    with open("input.txt", "r") as file:
        disk_input = file.read()

    disk_layout = []  # Represents the block-by-block structure of the disk
    file_id = 0

    for index, block_size in enumerate(disk_input):
        block_size = int(block_size)
        if index & 1 == 0:  # Even index represents file blocks
            disk_layout += [file_id] * block_size
            file_id += 1
        else:  # Odd index represents free space blocks
            disk_layout += ['.'] * block_size

    left, right= 0, len(disk_layout) - 1

    while left < right:
        while disk_layout[left] != '.':
            left += 1
        while disk_layout[right] == '.':
            right -= 1
        if left < right:
            disk_layout[left], disk_layout[right] = disk_layout[right], disk_layout[left],

    # Trim off trailing free space
    disk_layout = disk_layout[:left]

    checksum = sum(index * file_id for index, file_id in enumerate(disk_layout))

    print(checksum)


if __name__ == '__main__':
    main()