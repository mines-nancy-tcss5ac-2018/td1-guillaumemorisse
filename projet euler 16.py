
def solve16(n):
    "Solve the 16th Euler problem"
    "The function returns the sum of each digit contained  in the number 2**n  "
    nbre = 1
    sum = 0
    for i in range(n):
        nbre = nbre * 2
    litteral = str(nbre)
    for elt in litteral:
        sum += int(elt)
    return sum

assert solve16(15) == 26
print(solve16(1000))
