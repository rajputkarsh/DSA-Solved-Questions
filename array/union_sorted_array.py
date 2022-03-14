
from typing import Set


def findUnion(arr1, arr2):
    
    return set(arr1).union(set(arr2))

def findIntersection(arr1, arr2):
    return set(arr1).intersection(set(arr2))

if __name__ == '__main__':
    
    arr1 = [6, 2, 2]
    arr2 = [85, 25, 1, 32, 54, 6]

    print(findUnion(arr1, arr2))
