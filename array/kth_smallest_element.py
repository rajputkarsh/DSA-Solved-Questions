from lib.MinHeap import MinHeap

if __name__ == '__main__':
    heap = MinHeap(9)

    heap.insert(2)
    heap.insert(9)
    heap.insert(3)
    heap.insert(5)
    heap.insert(1)
    heap.insert(7)
    heap.insert(4)
    heap.insert(6)
    heap.insert(8)

    k = int(input("Enter k : "))

    data = 0
    for i in range(k):
        data = heap.removeMin();

    print("Minimum K-th element : ", data)