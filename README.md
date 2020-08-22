# Sorting Algorithms
Compare sorting algorithms with different unsorted lists.

## How to run it
This project uses docker and it contains a Makefile to be easier to build the image, 
run the tests and the script to compare the algorithms.

#### Initialize the docker container and run the unit tests:
`make deploy`

#### Run the script to compare the algorithms:
`make run`

## Algorithms
* **Bubble sort**: It works by checking each element of the list to be sorted with the next one, 
swapping them if they are in the wrong order. 
The entire list needs to be reviewed several times until no more exchanges are needed.  
Best case: O(n)  
Worst case: O(n2)  
Average case: O(n2)

* **Insertion sort**: Initially we have only one element, which is obviously an ordered set. 
Then, when there are k elements ordered, the element k + 1 is taken and compared with all the elements already ordered, 
stopping when a minor element or when no elements are found anymore. 
At this point the element k + 1 is inserted and the other elements must be moved.  
Best case: O(n)  
Worst case: O(n2)  
Average case: O(n2)

* **Selection sort**: The smallest element is selected from the unsorted array and swapped with the leftmost element 
and that element becomes part of the ordered array. 
This process continues moving unsorted array boundary by one element to the right.  
Best case: O(n)  
Worst case: O(n2)  
Average case: O(n2)

* **Merge sort**: Divide and conquer algorithm. 
The list is divided into two sublists of length/2 elements recursively until only one element remains 
and at the end all the sublists are merged sorted.
It's faster than quick sort in case of larger lists.  
Best case: O(nlogn)  
Worst case: O(nlogn)  
Average case: O(nlogn)

* **Quick sort**: Divide and conquer algorithm. 
The list is divided into two sublists recursively. 
It uses a pivot for partitioning the elements, the left partition contains the elements smaller than the pivot 
and the right partition contains the elements greater than the pivot.
It's faster than merge sort in case of smaller lists.  
Best case: O(nlogn)  
Worst case: O(n2)  
Average case: O(nlogn)

* **Heap sort**: This algorithm consists of storing all the elements of the vector to be ordered in a heap
and then extracting the node that remains as the root node of the heap (top) in successive iterations, 
obtaining the ordered set.  
Best case: O(nlogn)  
Worst case: O(nlogn)  
Average case: O(nlogn)