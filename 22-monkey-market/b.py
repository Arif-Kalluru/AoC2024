def process_secret(secret, N):
    prices = [0] * N
    changes = [0] * N
    prev = 0
    for i in range(N):
        remainder = secret % 10
        prices[i] = remainder
        changes[i] = str(remainder - prev)
        secret = (secret ^ (secret << 6)) & 0xFFFFFF
        secret = (secret ^ (secret >> 5)) & 0xFFFFFF
        secret = (secret ^ (secret << 11)) & 0xFFFFFF
        prev = remainder
    return prices, changes

def main():
    N = 2001
    sequences = []

    with open("input.txt", "r") as file:
        nums = [int(line.rstrip()) for line in file]

    for num in nums:
        prices, changes = process_secret(num, N)
        seq_map = {}

        for i in range(3, N):
            subsequence = ''.join(changes[i-3:i+1])
            if subsequence not in seq_map:
                seq_map[subsequence] = prices[i]

        sequences.append(seq_map)

    combined_seq_values = {}
    for seq_map in sequences:
        for seq, price in seq_map.items():
            combined_seq_values[seq] = combined_seq_values.get(seq, 0) + price

    result = max(combined_seq_values.values(), default=0)
    print(result)

if __name__ == '__main__':
    main()