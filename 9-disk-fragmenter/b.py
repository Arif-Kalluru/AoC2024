def main():
    with open("input.txt", "r") as file:
        disk_str = file.read()

    disk_layout = []  # Represents the disk's block structure
    files_metadata = []  # List of tuples (file_id, file_size)
    file_id = 0

    # Extract file sizes from the input and store metadata
    for i, block_size in enumerate(disk_str):
        block_size = int(block_size)
        if i % 2 == 0:  # Even index indicates file block
            files_metadata.append((file_id, block_size))
            file_id += 1

    # Reverse the metadata list for prioritizing larger file IDs during allocation
    files_metadata.reverse()
    processed_files = set()  # Tracks files that have been placed correctly

    current_file_id = 0
    for i, block_size in enumerate(disk_str):
        block_size = int(block_size)
        if i & 1 == 0:  # File block
            if current_file_id not in processed_files:  # File not yet processed
                # Add the file to the disk layout
                disk_layout += [current_file_id] * block_size
                processed_files.add(current_file_id)
            else:
                # File already processed; mark space as empty
                disk_layout += ['.'] * block_size
            current_file_id += 1
        else:  # Free space block
            # Attempt to fill the free space with remaining files
            while True:
                space_filled = False
                for j, (file_id, file_size) in enumerate(files_metadata):
                    if file_id in processed_files or file_size > block_size:
                        continue  # Skip files that are already placed or too large
                    # Place the file and update free space
                    disk_layout += [file_id] * file_size
                    block_size -= file_size
                    processed_files.add(file_id)
                    space_filled = True
                if not space_filled:  # If no files fit, stop filling
                    break
            # Add remaining free space as empty blocks
            disk_layout += ['.'] * block_size

    checksum = 0
    for index, block in enumerate(disk_layout):
        if block != '.':
            checksum += index * block

    print(checksum)


if __name__ == '__main__':
    main()