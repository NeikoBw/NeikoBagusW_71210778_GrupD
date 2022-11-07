class PriorityQueueSortedList:
    def __init__(self):
        self._data = []
    
    def peek(self):
        print(self._data[0])

    def add(self, next, prev):
        if len(self._data):
            pointer = 0
            while self._data[pointer][1] < prev:
                pointer += 1
            self._data.insert(pointer, (next, prev))
        else:
            self._data.append((next, prev))

    def update(self, prev, next):
        pointer = 0
        while self._data[pointer][1] != prev:
            pointer += 1
        self._data[pointer] = (next, prev)
    
    def remove(self):
        del self._data[0]

    def removePriority(self, prev):
        print("Data Prioritas Tertinggi :",end="")
        pointer = 0
        while self._data[pointer][1] != prev:
            pointer += 1
        del self._data[pointer]

    def printIsiQueue(self):
        print("Isi semua Queue: ", end="")
        for i in self._data[:-1]:
            print("{}," .format(i), end=" ")
        print("{}" .format(self._data[-1]))

#TEST CASE
sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)

sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")

sortedList.remove()
sortedList.removePriority(4)

sortedList.peek()
sortedList.printIsiQueue()