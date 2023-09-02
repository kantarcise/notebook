This chapter is all about PriorityQueues, Heaps, Selection - Insertion - Heap Sort and Adaptable Priority Queues. 

# Priority Queues

We need something more complex than a Queue for an Air Traffic Controller because there are a lot of things to think about before letting a plane land or takeoff (remaining fuel, time waited, distance from runway). So we make Priority Queues.

- `add(key, value)`
- `P.add(5, A)` -> `[(5, A)]`
- `P.add(9, C)` -> `[(5, A), (9, C)]`
- `P.add(3, B)` -> `[(3, B), (5, A), (9, C)]`
- `P.add(7, D)` -> `[(3, B), (5, A), (7, D), (9, C)]`
- `P.min()` -> `(3, B)`
- `P.remove_min()` -> `(3, B)`
- `P.remove_min()` -> `(5, A)`
- `len(P)` -> `2`
- `P.remove_min()` -> Error
- `P.is_empty()` -> `True`
- `P.remove_min()` -> Error

## We can implement PriorityQueues with Unsorted or Sorted Lists

For unsorted list:
- `min()` or `remove_min()` will be O(n) linear time - we have to inspect all entries.
- `add()` takes O(1) time - because we just add to the end of the list.

For a sorted list:
- `min()` and `remove_min()` take O(1) time with a DoublyLinkedList.
- But now `add()` takes O(n) time because we need to find the appropriate position for the new element.

## Heaps - O(log n) time insert and remove

A more efficient realization of a priority queue using a data structure called a binary heap. This data structure allows us to perform both insertions and removals in logarithmic time, which is a significant improvement over the list-based implementations.

The fundamental way the heap achieves this improvement is to use the structure of a binary tree to find a compromise between elements being entirely unsorted and perfectly sorted.

### Heap-Order Property
In a heap T, for every position p other than the root, the key stored at p is greater than or equal to the key stored at p's parent. A minimum key is always stored at the root of T.

### Complete Binary Tree Property
A heap T with height h is a complete binary tree if levels 0, 1, 2, ..., h - 1 of T have the maximum number of nodes possible (level i has 2^i nodes, for 0 ≤ i ≤ h - 1), and the remaining nodes at level h reside in the leftmost possible positions at that level.

## Selection Sort

If we implement PQ with an unsorted list:

Phase 1 of pq sort takes O(n) time, for we can add each element in O(1) time. Phase 2 where we repeatedly remove an entry with the smallest key from the priority queue P. The size of P starts at n and incrementally decreases with each remove_min until it becomes 0. O(n^2) time.

The running time of each remove_min operation is proportional to the size of P. Thus, the bottleneck computation is the repeated "selection" of the minimum element in Phase 2. For this reason, this algorithm is better known as selection-sort.

## Insertion Sort

If we implement the priority queue P using a sorted list:

Then we improve the running time of Phase 2 to O(n), for each remove_min operation on P now takes O(1) time. Unfortunately, Phase 1 becomes the bottleneck for the running time since, in the worst case, each add operation takes time proportional to the current size of P. This sorting algorithm is better known as insertion-sort.

## AdaptablePriorityQueue - Update and Remove

AdaptablePriorityQueue enables us to perform update and remove operations in logarithmic time.


