import fileinput
import math



if __name__ == "__main__":
    testCases = []
    for lines in fileinput.input():
        testCases.append(int(lines.rstrip()))

    for case in testCases:
        if case == 0:
            break
        # the nth number is already known to give explosion
        case = case - 1
        # by triangle equation
        n = math.ceil((math.sqrt(8*case + 1) - 1) / 2)
        print(n)
