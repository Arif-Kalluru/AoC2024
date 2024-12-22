def process_secret(secret):
    # 16777216 is 0xFFFFFF (1 << 24)
    for _ in range(2000):
        secret = (secret ^ (secret << 6)) & 0xFFFFFF
        secret = (secret ^ (secret >> 5)) & 0xFFFFFF
        secret = (secret ^ (secret << 11)) & 0xFFFFFF
    return secret

def main():
    result = 0
    with open("input.txt", "r") as file:
        nums = [int(line.rstrip()) for line in file]
    
    result = sum(process_secret(num) for num in nums)

    print(result)

if __name__ == '__main__':
    main()