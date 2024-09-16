class Task:

    def __init__(self, taskId, priority, arrivalTime, deadline) -> None:
        self.taskId = taskId
        self.priority = priority
        self.arrivalTime = arrivalTime
        self.deadline = deadline

class Queue:

    def __init__(self) -> None:
        self.arr = []

    #creating a max heap
    def heapify(self, A, k ,i):
        max = i #index of root node (lets assume this is largest)
        left = 2 * i  +1#for i as root
        right = 2 * i + 2#for i as root
    
        if left < k and A[left].priority > A[max].priority:
            max = left

        if right < k and A[right].priority > A[max].priority:
            max = right

        if max != i: # changing the root to the largest element from left vs right node
            A[max], A[i] = A[i], A[max]
            self.heapify(A, k, max)


    def insert(self, A):

        self.arr.append(A)

        for i in range(len(self.arr) // 2 -1, -1, -1): #creating a max heap
            self.heapify(self.arr, len(self.arr), i)

        return
    
    # swap the lowest priority ( which is always in second half) with last element and remove the last element and heapify
    def remove_least_priority_task(self):

        if self.is_empty():
            return "The heap is empty."
        
        lowestPriority = self.arr[len(self.arr) // 2 - 1]

        for i in range(len(self.arr) // 2, len(self.arr)):
            if self.arr[i].priority < lowestPriority.priority:
                lowestPriority = self.arr[i]

        index_least_priority_task = self.arr.index(lowestPriority)

        self.arr[len(self.arr)-1], self.arr[index_least_priority_task] = self.arr[index_least_priority_task], self.arr[len(self.arr)-1]


        print(f"Removing lowest priority task: {queue.arr[len(self.arr)-1].priority} for deadline {queue.arr[len(self.arr)-1].deadline}") # For max hea, the first element or the root element is the highest priority

        self.arr.pop()
        
        self.heapify(self.arr, len(self.arr), len(self.arr)-1 // 2)


        return lowestPriority 


    #simple swap the root element which is the first element in heap with last element and remove the alst element and heapify
    def remove_highest_priority_task(self):  
             
        if self.is_empty():
            return "The heap is empty."
        
        self.arr[0], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[0]

        print(f"Removing highest priority task: {queue.arr[len(self.arr)-1].priority} for deadline {queue.arr[len(self.arr)-1].deadline}") # For max hea, the first element or the root element is the highest priority
        
        self.arr.pop()
        
        self.heapify(self.arr, len(self.arr), 0)



    def modify_priority(self, taskId, new_priority):

        for i in range(0, len(self.arr)): #check for the array where it has same priority and update with new priority
            if self.arr[i].taskId == taskId:
                self.arr[i].priority = new_priority

                for i in range(len(self.arr) // 2 -1, -1, -1): #loop throught the index to retrieve max heap property
                    self.heapify(self.arr, len(self.arr) ,i)

        return


    def is_empty(self): #check if the heap is empty
        return len(self.arr) == 0


queue = Queue()

queue.insert(Task(11, 1, "09:00", "17:00"))
queue.insert(Task(22, 2, "08:00", "18:00"))
queue.insert(Task(33, 3, "07:00", "19:00"))
queue.insert(Task(44, 4, "06:00", "20:00"))
queue.insert(Task(55, 5, "05:00", "21:00"))
queue.insert(Task(66, 6, "04:00", "22:00"))
queue.insert(Task(77, 7, "04:00", "23:00"))
queue.insert(Task(88, 8, "04:00", "24:00"))
queue.insert(Task(99, 9, "04:00", "02:00"))
queue.insert(Task(100, 10, "04:00", "01:00"))

print(f"\n Afterinserting\nHighest priority is {queue.arr[0].priority} for deadline {queue.arr[0].deadline}")
print(f"Priority is {queue.arr[1].priority} for deadline {queue.arr[1].deadline}")
print(f"Priority is {queue.arr[2].priority} for deadline {queue.arr[2].deadline}")
print(f"Priority is {queue.arr[3].priority} for deadline {queue.arr[3].deadline}")
print(f"Priority is {queue.arr[4].priority} for deadline {queue.arr[4].deadline}")
print(f"Priority is {queue.arr[5].priority} for deadline {queue.arr[5].deadline}")
print(f"Priority is {queue.arr[6].priority} for deadline {queue.arr[6].deadline}")
print(f"Priority is {queue.arr[7].priority} for deadline {queue.arr[7].deadline}")
print(f"Priority is {queue.arr[8].priority} for deadline {queue.arr[8].deadline}")
print(f"Priority is {queue.arr[9].priority} for deadline {queue.arr[9].deadline}")


print("\n")
queue.remove_highest_priority_task() # For max heap, the first element or the root element is the highest priority
queue.remove_least_priority_task()

print(f"\nHighest priority is {queue.arr[0].priority} for deadline {queue.arr[0].deadline}")
print(f"Priority is {queue.arr[1].priority} for deadline {queue.arr[1].deadline}")
print(f"Priority is {queue.arr[2].priority} for deadline {queue.arr[2].deadline}")
print(f"Priority is {queue.arr[3].priority} for deadline {queue.arr[3].deadline}")
print(f"Priority is {queue.arr[4].priority} for deadline {queue.arr[4].deadline}")
print(f"Priority is {queue.arr[5].priority} for deadline {queue.arr[5].deadline}")
print(f"Priority is {queue.arr[6].priority} for deadline {queue.arr[6].deadline}")
print(f"Priority is {queue.arr[7].priority} for deadline {queue.arr[7].deadline}")

queue.modify_priority(33, 9)
queue.modify_priority(77, 1)

print("\nAfter modifying:")
print(f"Highest priority for id {queue.arr[0].taskId} is {queue.arr[0].priority} for deadline {queue.arr[0].deadline}")
print(f"Priority for id {queue.arr[1].taskId} is {queue.arr[1].priority} for deadline {queue.arr[1].deadline}")
print(f"Priority for id {queue.arr[2].taskId} is {queue.arr[2].priority} for deadline {queue.arr[2].deadline}")
print(f"Priority for id {queue.arr[3].taskId} is {queue.arr[3].priority} for deadline {queue.arr[3].deadline}")
print(f"Priority for id {queue.arr[4].taskId} is {queue.arr[4].priority} for deadline {queue.arr[4].deadline}")
print(f"Priority for id {queue.arr[5].taskId} is {queue.arr[5].priority} for deadline {queue.arr[5].deadline}")
print(f"Priority for id {queue.arr[6].taskId} is {queue.arr[6].priority} for deadline {queue.arr[6].deadline}")
print(f"Priority for id {queue.arr[7].taskId} is {queue.arr[7].priority} for deadline {queue.arr[7].deadline}")

        