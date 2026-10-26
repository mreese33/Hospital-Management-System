
class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []


    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = (
                    self.data[parent_index], self.data[index]
                )
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left

            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest], self.data[index]
            )

            index = smallest

    def insert(self, patient):
        if not 1 <= patient.urgency <= 10:
            print("Urgency must be between 1 and 10.")
            return

        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("\nCurrent Queue:")

        if len(self.data) == 0:
            print("No patients in the queue.")
            return

        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        if len(self.data) == 0:
            return None

        return self.data[0]

    def remove_min(self):
        if len(self.data) == 0:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        most_urgent = self.data[0]

        self.data[0] = self.data.pop()

        self.heapify_down(0)

        return most_urgent


# Test the Patient and MinHeap classes
patient1 = Patient("Riley", 2)
patient2 = Patient("Jordan", 5)

heap = MinHeap()

print("Patient 1:", patient1.name, patient1.urgency)
print("Patient 2:", patient2.name, patient2.urgency)
print("Current heap:", heap.data)

# Test the emergency priority queue
heap = MinHeap()

heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))

heap.print_heap()

# Check the most urgent patient
next_up = heap.peek()
print("\nNext Patient:", next_up.name, next_up.urgency)

# Remove the most urgent patient
served = heap.remove_min()
print("\nPatient Served:", served.name)

# Print the updated queue
heap.print_heap()

# Check the most urgent patient
next_up = heap.peek()
print("\nNext Patient:", next_up.name, next_up.urgency)

# Remove the most urgent patient
served = heap.remove_min()
print("\nPatient Served:", served.name)

# Print the updated queue
heap.print_heap()

# Test edge cases
print("\nTesting Edge Cases:")

# Test an invalid urgency level
heap.insert(Patient("Morgan", 12))

# Test removing patients until the queue is empty
while heap.peek() is not None:
    served = heap.remove_min()
    print("Patient Served:", served.name)

# Test an empty queue
print("Peek Empty Queue:", heap.peek())
print("Remove Empty Queue:", heap.remove_min())

heap.print_heap()
