answers = []
equations = []

# Returns True if it was possible to solve the equation
def solve(answer, result, eq_idx, idx) -> bool:
    equation = equations[eq_idx]
    if idx == len(equation):
        return answer == result
    add = solve(answer, result + equation[idx], eq_idx, idx + 1)
    multiply = solve(answer, result * equation[idx], eq_idx, idx + 1)
    return add or multiply
    
def main():
    with open("input.txt", "r") as file:
        for line in file:
            line = line.rstrip().split(':')
            answers.append(int(line[0]))
            equations.append([int(n) for n in line[1].split()])

    total = 0

    for i in range(len(answers)):
        result = equations[i][0]
        answer = answers[i]
        if solve(answer, result, i, 1):
            total += answer

    print(total)

if __name__ == '__main__':
    main()