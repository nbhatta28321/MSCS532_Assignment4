
import random
import time

#creating a max heap
def heapify(A, k ,i):
    max = i #index of root node (lets assume this is largest)
    left = 2 * i +1#for i as root
    right = 2 * i + 2 #for i as root

   
    if left < k and A[left] > A[max]:
        max = left

    if right < k and A[right] > A[max]:
        max = right

    if max != i: # changing the root to the largest element from left vs right node
        A[max], A[i] = A[i], A[max]
        heapify(A, k, max)    

def heapSort(A):
    for i in range(len(A) // 2 -1, -1, -1): #loop throught the index and building a heap
        heapify(A, len(A) ,i)

    for i in range(len(A)-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i ,0)

num=100000

   
# function to do the merge sort for random variables
start = time.time()
heapSort([random.randint(1, 50) for _ in range(num)])
end = time.time()
print(f"Execution time for random numbers is {end-start} where number of elements is {num}")

start = time.time()
heapSort(list(range(num)))
end = time.time()
print(f"Execution time for sorted numbers is {end-start} where number of elements is {num}")

start = time.time()
heapSort(list(range(num, 0, -1)))
end = time.time()
print(f"Execution time for reverse sorted numbers is {end-start} where number of elements is {num}")

start = time.time()
a =heapSort([15 for _ in range(num)]) # array of repeated element
end = time.time()
print(f"Execution time for repeated elemets is {end-start} where number of elements is {num}")