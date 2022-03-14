
class MinHeap:
    def __init__(self, capacity):
        self.storage = [0]*capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        return (index-1) // 2

    def getLeftChildIndex(self, index):
        return (index*2) + 1

    def getRightChildIndex(self, index):
        return (index*2) + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def insert(self, data):
        if (self.isFull()):
            raise Exception("Heap is Full")

        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)

    def removeMin(self):
        if self.size == 0:
            raise Exception("Heap is empty")

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)

        return data


    def heapifyUp(self, index):
        if self.hasParent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))

    def heapifyDown(self, index):

        # get smaller element between children
        smallest = index
        if self.hasLeftChild(index) and self.storage[smallest] > self.leftChild(index):
            smallest = self.getLeftChildIndex(index)
            
        if self.hasRightChild(index) and self.storage[smallest] > self.rightChild(index):
            smallest = self.getRightChildIndex(index)

        if smallest != index:
            self.swap(index, smallest)
            self.heapifyDown(smallest)
