
import math

def findWrap(words, limit):
    costArray = [ [-1 for i in range(len(words))] for j in range(len(words))]

    for i in range(len(words)):
        for j in range(i, len(words)):
            wordsRequired = sum(words[i:j+1]) + j-i
            if wordsRequired <= limit:
                costArray[i][j] = (limit-wordsRequired)*(limit-wordsRequired)
            else:
                costArray[i][j] = float("inf")

    for arr in costArray:
        print(arr)

    minCost   = [float('inf') for i in range(len(words))]
    finalCost = [float('inf') for i in range(len(words))]

    for i in range(len(words)-1, -1, -1):
        minCost[i] = costArray[i][len(words)-1]
        finalCost[i] = len(words)

        for j in range(len(words)-1, i, -1):
            if costArray[i][j-1] == float('inf'):
                continue

            if minCost[i] > minCost[j] + costArray[i][j-1] :
                minCost[i] = minCost[j] + costArray[i][j-1]
                finalCost[i] = j

    print(minCost)
    print(finalCost)

    return minCost[0]


if __name__ == "__main__":
    words = [3, 2, 2, 5]
    limit = 6
    findWrap(words, limit)