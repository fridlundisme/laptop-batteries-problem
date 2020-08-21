import numpy as np
import math

ten = np.array([1,2,3,4,5,6,7,8,9])
twtre = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])


def splitThird(array, n):
    if(len(array) <= 4):
        print("End recursion " + str(len(array) - 1))
        return len(array) - 1
    else:
        oneThird = math.floor(len(array)/3)
        array1 = array[0:oneThird]
        array2 = array[oneThird+1:None]

        print(array1)
        print(array2)
        n += 1
        print("iterations " + str(n))
        return n + splitThird(array2, n)



en = splitThird(ten, 0)
print(en)
