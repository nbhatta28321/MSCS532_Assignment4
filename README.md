# How to run:
> python3 ./heapSort.py
> python3 ./priorityQueue.py


# Heapsort

Heap sort uses a full binary tree to sort the number based on the maximum or minimum heap. This involves building a binary tree or arranging the element in a maximum or minimum heap. This involved using a root node, comparing its adjacent child node, and swapping if the child nodes are larger than the root node. Then, we move the pointer to one element less than the size of the array and iteratively move through the other element to sort the element. The best case for heap sort would be when the element is identical. It does not have to heapify; it just has to check the elements once. Each element would have a constant time of O(1), so the best-case time complexity would be O(nlogn) since it still checks to the maximum element. In other cases, heapSort involves heapifying the root extracting the maximum element from the heap, and repeating the process until moving all the way through the nodes in the tree. The time complexity for building a maximum heap for all the nodes in the tree has the time complexity of O(n), where n is the number of elements in the heap. Secondly, extracting the maximum element takes the time complexity of O(1), and going through all n nodes with the height of the tree requires the time complexity of O(nlog.n) The worst-case time complexity of the heap Sort is also same as an average case since it still goes over all the elements and checks if its larger than he root node when building a max-heap. From the above illustration, it is clear that the heap sort arranges the elements by extracting each element and checking the largest element from the left and right child nodes, so for worst, average, and best cases, the heapsort takes the time complexity of O(n log n). Heap sort has a space complexity of O(1) since the elements are rearranged recursively. It arranges the sorted element while heapifying and sorting the element further as well.


The heap sort was run through different element numbers, and the execution time was observed for 10000 and 100000 elements. It was running through random, sorted, reverse-sorted, and repeated elements.
```
Execution time for random numbers is 0.01971888542175293 where number of elements is 10000
Execution time for sorted numbers is 0.018770933151245117 where number of elements is 10000
Execution time for reverse sorted numbers is 0.016388893127441406 where number of elements is 10000
Execution time for repeated elemets is 0.002117156982421875 where number of elements is 10000
```
```
Execution time for random numbers is 0.49544215202331543 where number of elements is 100000
Execution time for sorted numbers is 0.30182504653930664 where number of elements is 100000
Execution time for reverse sorted numbers is 0.28430604934692383 where number of elements is 100000
Execution time for repeated elemets is 0.024802207946777344 where number of elements is 100000
```

From the above data, it is clear that the time execution of sorted and reverse sorted was better than random elements. The best time execution was for the repeated elements since it does not have to go through check and update the maximum number when typifying the tree. From the above, we can visualize that in the real-world scenario, the data are sorted, and for the max heap, the reversely sorted array gives a better execution time. That infers that we can implement the heap as a min-heap, which will have a good time complexity for sorted elements. 

When comparing the results above to QuickSort and MergeSort, QuickSort performed better than heapsort and MergeSort for random elements and sorted elements in both scenarios of 10000 and 100000. Even with reverse order, the quick sort was faster than the heap sort. Since Quick Sort does not swap elements when the order is correct, sorting numbers from different data sets becomes advantageous when the pivot element is taken correctly. Hence when we need a garauntee result, heap Sort is more reliable and memory efficient, Quick sort is faster to sort elements of various distribution of elements.

# Priority Queue

Priority Queue uses the heap data structure to retrieve the data based on the priority index given the instance of an object. In this case, it is the class Task. An array can be used to create a heap, which can be used for different operations. The insertion in the max heap is done by adding an n element to the tree of height O(logn). So the total time complexity of adding n element in a priority queue is O(nlogn). In the priority queue, a max is created to implement the queue. Extracting the highest element or the root node takes a time complexity of O(1) since it is a root node in the tree. To remove the highest element or root node, we have to swap the root node with the last element of the tree to maintain the property of a complete tree. Then we remove the element from the last node and heapify the element to maintain the max-heap property. This has a time complexity of O(logn). Deleting any instance of an object or the priority in the priority queue has a time complexity of O(logn) since it takes O(n) time to search for the priority, and we have to swap it to the last element and heapify to retain the property of the max heap. 

Removing the least priority of the task in the maximum heap takes O(logn). For a maximum heap, the highest element or, in this case, the field "priority" in the Object is the root node or parent node in the array as a heap. This is easier to observe; however, the least element has to be looked through the heap. Since the tree is arranged so that the leaf node is smaller than its parent node, the least element has to lie in the second half of the max heap. This will save the execution time to half when searching for the least priority element. When the least priority element is extracted, we swap the value to the last element and remove it from the heap. Then we must heapify the array to make it into a max heap. Similarly modifying the priority in the Queue requires the time complexity of O(logn). This requires going through all the elements to check for the same task_id, which requires the time complexity of O(n). Then, after the task_id matches, it goes through all the nodes to heapify, which has a time complexity of O(n) since it goes through the loop and creates a max heap for the n element. 

In conclusion, a priority queue is useful for assigning an element with a priority, which makes the execution time for a priority element fast. From the implementation, there are a lot more optimizations, which I noticed, such as avoiding building the entire tree as a max heap when the priority is reassigned. Instead, build a heap up or heap down method to heapify based on the priority less or more than the current element.

