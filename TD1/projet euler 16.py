def solve(n):
    "The function returns the sum of each digit contained  in the number 2**n  "
    nbre = 1
    sum = 0
    for i in range(n):
        nbre = nbre * 2
    for digit in str(nbre):
        sum += int(digit)
    return sum


assert solve(15) == 26

print(solve(1000))