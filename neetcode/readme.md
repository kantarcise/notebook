# [The Perfect Hour.](https://youtu.be/WkfkMTEqQak?t=904)

## Arrays & Hashing

- 001.containsDuplicate:
  - You can use a hash map and get the maxOccurance from values. (freq dict , ***max_occurance = max(freq.values()***)
  -
  - CAREFUL - ***max (dict , key=dict.get())*** WILL GIVE YOU THE KEY not the VALUE
  -
  - You can use greedy approach and exit as soon as you find something occuring twice.
  -
  - You can use sets, which has ***add()*** and ***remove()*** methods.
 
- 002.isAnagram:
  - collections has Counter, which is wonderful.
  -
  - The Counter() function takes a sequence as input and returns a dictionary that maps each element in the sequence to its frequency.
  -
  - You can use a hash map, to count the frequency for the first sequence, and delete one by one for the second sequence. In the end. expect the hashmap to be empty.
  -
  - For first seq:
  - ***char_count[char] = char_count.get(char, 0 ) + 1***
  - 
  - For second seq:
  - ***char_count[char] -= 1      if char_count[char] == 0:      del char_count[char]***

- 003.twoSum:
  - Basic idea is to use elements and find the remainder from the target.
  -
  - ***index()*** can be used with a START index to find the (possibly) second element - terrible complexity o(n)
  - 
  - You can use a hashmap, for elements and their indexes.
  - 
  - Never forget: ***for index, elem in enumerate(sequence)***


- 004.groupAnagrams:

  - We can use a dictionary to keep key value relationships 
  between sequence elements and their Counters
  -
  - We can sort all elements in sequence to unify the frequency of characters
  -
  - if not seen before in the dictionary, we can initialize an empty list
    later to append on it.


- 005.topKFrequent:

  - USE COLLECTIONS. A library that is written by competent 
people is way better your weird approach.
  -
  - Collections Counter is pretty cool. Dict subclass for counting hashable items.
  - Sometimes called a bag or multiset.  Elements are stored
  -  as dictionary keys and their counts are stored as dictionary values.
  -
  - COunter has most_common method.
  - 
  - List the n most common elements and their counts from the most 
    common to the least. If n is None, then list all element counts.

- 006.productExceptSelf:

  - If you multiply every element to the left and to the right, 
you will get the product of all elements.
  - 
  - result = [1] * n   # why?
  -
  - Space Allocation: Preallocating a list with a known length can be more memory-efficient compared to dynamically adding elements one by one, especially when you know the maximum size of the list in advance.
  -
  - Performance: In some cases, creating a list with a default value can be faster than appending elements to an empty list, especially when dealing with a large number of elements.
 
 
- 007.isValidSudoku:

  - compartmentalize of the code is the single greatest thing you can learn.
  -
  - zip() can be usec to combine multiple sequences iwth respect to their index.\

  - zip() function is used to combine two or more lists (or any other iterables) into a single iterable, where elements from corresponding positions are paired together.

  - unzipping values:

  - To unzip something zipped, use * on it just like tuple unpacking  namz, roll_noz, marksz = zip(*mapped)
  
  - Here is something interesting:
  - ```
    a,b,c,d,*e, f  = range(10)
    a = 0
    b = 1
    c = 2
    d = 3
    e = [4,5,6,7,8]
    f = 9
    ```
  - also don't forget, you have map(), filter() and lambda x : x**2 ready to go.
 
- 008.encodeDecode:

  -  We are trying to encode decode stateless. So we somehow need to  clarify the word lenghts while we are trasporting them.
  - 
  - for that we can use the lenght of the words and sent them prior to the encoded words.
  - 
  - When we are decoding, we will know how many indexes we need to be  looking for, simply using the length.
 
- 009.longestConsecutive:

  - to get rid of reapparent values, you can use a set,
  -
  - imply defining the question in ENGLISH is the first step. Meaning write the pseudo CODE First.
  -
  - you can override a value in an iteration with
  -
  -   current = max(current, new)

## Two Pointers
 
- 010.isPalindrome:

  - Palindrome simply means that reverse of the string is equal to original string
  -
  - strings have wonderful methods:
  -
  - string.isalpha()        and         string.lower()
  -
  - str_seq[::-1] is reversed of str_seq
  -
  - Other wonderful string methods:
  -
  - string.strip() , string.split() , string.capitalize()
  -
  - string.isdigit(), string.title(), string.starswith(), string.endswith()
  -
  - You can use two pointers approach
  -
  - In this example, this basically means to check some conditions for each of the pointers and progress both of them.
 
- 011.twoSumSortedSequence:

  - enumerate is still one of the best ways to traverse a sequence.
  -
  - YOu can and you should use dictinaries whenever you want to store and access a value/key combination.
 
- 012.3Sum:
  
  - Two pointer approach is simple. you define them and you set up conditions on their changes.
  - 
  - Updating a sequence on the fly is NOT HELPFUL so far. No Removes no copying lists  please.
  -
  - Solid effort on compartmentalizing. Defining the object which you are thinking to return is a good and simple idea.

- 013.containerwithmostwater:

  - Brute Force can help you find a pattern in which you can expand on.
  - 
  - Two pointers keep being the same, define them first and on condition
 increase/ decrease them.

- 014.trapping_rain_water:

  - two pointers are still doing wonders.
  -
  - trying to find a pattern for each step is the key for approaching these problems.
  -
  - you need to be calm. you will be calm when you solve your 250th question.
  -
  - just a numbers game

## Stack

- 015.valid_paranthesis:

  - matching symbols is just asking for a hash map to be used
  - 
  - we are using a stack for storing all of the opening brackets.
  - 
  - For each closing bracket we are looking for the last element 
  - in stack to be matched by the closing symbol
  - 
  - if everything went smooth, stack should be empty in the end.

- 016.min_stack:

  - The key takeaway from this code is that by maintaining an auxiliary data structure
  - specifically designed to handle the minimum value, you can achieve O(1) time
  - complexity for the getMin() operation while still supporting standard stack operations.
  - 
  - The choice between array-based and linked-list-based approaches depends on
  - your preference and specific use case.
  - 
  - lists has append, push, pop methods. As usual.
 

- 017.evaluate_reverse_polish_notation:

  - Use a stack
  -
  - compartmentalize the code.
  -
  - you can use the same stack for both operations and operands.
  - 
  - ```for c in tokens: if + - / * else stack.append(int(c))```
  -
  - It is possible to use dictionaries aswell.

- 018.generate_parantheses:

  - Well-formed parentheses combinations have an equal number of
  - opening '(' and closing ')' parentheses.
  -
  - You need to ensure that at any point while generating combinations, the
  - number of closing ')' parentheses does not exceed the number of
  - opening '(' parentheses.
  -
  - The code demonstrates a backtracking approach, which is a common technique
  - for generating combinations recursively.
  -
  - The generateParenthesis method uses a backtracking algorithm and a stack
  - (stack) to keep track of the current combination. It recursively generates
  - combinations, adding '(' when possible and ')' when it meets the criteria.
  - 
  - The idea is to add ')' only after valid '('
  - We use two integer variables left & right to see how many '(' & ')' are in the current string
  - If left < n then we can add '(' to the current string
  - If right < left then we can add ')' to the current string


- 019.daily_temperatures:

  - To hold the previous values while traversing a list, a list or a stack can be useful.
  -
  - Initialize the result list, as it is simply the same size as the given sequence.
  -
  - while control flow is wonderful with more than one booleans. Try to
  - perfect the iteration with multiple conditions


- 020.car_fleet:

  - Car that is closest to the target is the bottleneck, becuase of this
  - reason, we traverse the sequence in reverse.
  -
  - we can use zip() to combine multiple lists as pairs = [positions, speed]
  -
  - ```pair = [[p, s] for p, s in zip(position, speed)]```
  -
  - We can use a stack to compare car duos
  -
  - Basically using the time that a car going to be at target with its
  - speed and whether or not the car behind it will catch up with it
 
- 021.largest_rectangle_in_histogram:

  - What is the limiter case? If there is a smaller rectangle limiting the
  - rectangle to extend beyond.
  -
  - Handling Decreasing Heights: When the current height is smaller than the height
  - at the top of the stack (i.e., stack[-1][1] > h), it means the current height
  - terminates a sequence of increasing heights. In this case, the code calculates
  - the area of rectangles formed by the heights in the sequence and updates th
  - maximum area found so far.
  -
  - the while loop:
  -
  - The while loop continues executing as long as there are elements in the stack
  - (i.e., while stack), which implies that it will run until the stack is empty.
  -
  - Stack Top Comparison: The condition inside the while loop, stack[-1][1] > h,
  - checks whether the height of the current bar (h) is smaller than the height
  - of the bar at the top of the stack. In other words, it checks if the current
  - bar represents the end of a sequence of increasing heights.
  -
  - Popping Elements: When the condition is met (i.e., the current bar's height
  - is smaller), the loop executes, and it repeatedly pops elements from the
  - stack until the condition is no longer met. This is done with the line
  - index, height = stack.pop().
  -
  - Updating Maximum Area: For each popped element, it calculates the area of the
  - rectangle formed by that height and the width of the sequence of increasing
  - heights that ended at the current position (i - index). The maximum area
  - (max_area) is updated whenever a larger area is found.

## Binary Search
 
- 022.binary_search:

  - Binary search, whether implemented iteratively or recursively, has a
  - time complexity of O(log n) because it continuously reduces the search
  - range by half with each comparison. This logarithmic time complexity
  - is significantly faster than linear time complexity (O(n)), especially
  - for large lists.
  -
  - In basic search, you can traverse the sequence but that would be O(n).
  - We use 2 pointers and check if target is equal to kinda middle of the
  - sequence so that we eliminate more than one value each loop. 

- 023.search_a_2d_matrix:

  - ```
    l, r = 0, len(seq) - 1
    mid = l + ((r-l)//2)
  - 
  - We dont have to iterate over all elements, not even every row.
  -
  - we can do double binary search to decide which row we are interested in
  - and search for the target
  -
  - This should be obvious also
  -
  - ```ROWS, COLS = len(matrix), len(matrix[0])```


- 024.koko_eating_bananas:

  - math.ceil for finding the ceiling of a number.
  -
  - understanding the question will give you a range for possible k values
  -
  - after that, we can apply binary search to that sequence!
  - this is cool:
  -
  - ``` mid = l + ((r - l) // 2)```

 
- 025.find_minimum_rotated_sorted_array:

  - If you see a O(log n ) in the question, instantly think of binary search.
  -
  - Because we know the sequence is sorted, rotated but sorted, we can use this to our advantage.
  -
  - If the mid we calculate is bigger than left pointer, then we are in the sorted part of left
  - so go to the right
  -
  - If the mid we calculate is smaller than right pointer, than we are in the sorted part of right
  - so go to the left for even smaller numbers.


- 026.search_in_rotated_sorted_array:

  - Any time you are looking for a log time complexity, you should look for binary search.
  -
  - For this question, it's like we have 2 sorted sequences combined.
  -
  - Look  at the picture before writing the code. Give 2 discrete
  - examples for different edge cases.


- 027.time_based_key_value_store:

  - You can use a default dict, but use a dict to make it simpler and more global.
  -
  - in setter, we simply check if the key we have is already inside the dictionary
  -
  - in getter, we use get method for default value, and use binary search to
  - find the value we are looking for (or the smaller closest to it in terms of timestamps) 


- 028.median_of_two_sorted_arrays:

  - We see the log(n) we think binary search.
  -
  - Extending and slicing a list is instantly o(N)
  -
  - We dont have to sort or extend the lists. we can just us the fact that
  - both sequences are sorted.
  -
  - The key condition for finding the median is that, for partitions:
  -
  - left x should be smaller or equal to right x
  - left y should be smaller or equal to right x


- 029.best_time_to_buy_and_sell_stock:

  - We are using a sliding window, with to pointers.
  -
  - Only moving right pointer is enough to traverse through
  -
  - check profit for each transaction, and update max
  -
  - if we find a new low, update left pointer.

- 030.longest_substring_without_repeating_characters:

  - Sets are great for duplicate questions
  -
  - For a sliding window, you still need to have two pointers
  -
  - With thinking about the worst case, you can set up conditions around it.

- 031.longest_repeating_character_replacement:

  - For a string,  we need to remember that there are 26 letters in
  - the English language
  -
  - we want to maximize the number of characters in the substring
  - to get to the max number of characters, we would want to replace
  - the characters that occurs the least. (less frequent)
  -
  - We need to setup a sliding window that changes its size based on the
  - number of characters we can replace (k) and the equation we know.
  -
  - for every substring, we can calculate the characters to be replaced by:
  - ```windowLen - count[mostFrequent]  <= k```
  - where count is a dictionary (hash map) with occurences of characters
  - 
 
- 032.permutation_in_string:

  - do not forget about edge cases.
  -
  - string character frequency is a GREAT usecase for Hashmaps
  -
  - comparing a sliding window for the target string can be an approach
  -
  - [1, 2, 3] != [3, 2, 1] - so use dictionaries

  
- 033.minimum_window_substring:

  - Using a hashmap is CLASSIC at this point, for frequency counters in strings
  - 
  - Here are some tips for using the sliding window algorithm to solve problems:
  - 
  - 1. Identify the condition that the substring must satisfy. 
  - This is the most important step, as it will determine how 
  - the algorithm is implemented.

  - 2. Initialize the sliding window. The sliding window can be 
  - initialized to be any size, but it is generally a good idea 
  - to start with a small window and then increase the size of the
  -  window as needed.

  - 3. Check whether the sliding window satisfies the condition.
  - This is the core of the sliding window algorithm. If the sliding
  - window satisfies the condition, then the algorithm has found a
  - substring that satisfies the condition.

  - 4. Update the sliding window. The sliding window can be updated by 
  - either incrementing the left pointer or the right pointer.
  -  Incrementing the left pointer will remove the leftmost character 
  -  from the window, while incrementing the right pointer will add 
  -  the next character to the window.

  - Repeat the process until the end of the string is reached. The 
  - algorithm should continue to iterate over the string until it reaches
  -  the end of the string. If the algorithm has not found a substring
  - that satisfies the condition by the time it reaches the end of
  - the string, then the algorithm should return an empty string.

- 034.sliding_window_maximum:

  - Pretty easy to solve in Exponential time
  -  
  - To solve it in linear time, we use deques
  - 
  - Both pointers can start from 0, right should be smaller than lenght of sequence.
  - 
  - For every window, append elements to the deque but pop 
  - all elements  if they are not bigger than current element
  - 
  - When you find the current max in the window, now you can update the left pointer

## Linked List

- 035.reverse_linked_list:

  - The main condition for Linked Lists is that while traversing, the
  - node will be not None
  -
  - TO reverse a LL, you need to make it go from
  -
  - 1 -> 2 -> 3 -> 4 -> 5 to 1 <- 2 <- 3 <- 4 <- 5
  -
  - Simplest way it to traverse every node and change directions of pointers
  -
  - When you are dealiong with a pointer, make sure you finish
  - all operations on it (prev, next)


- 036.merge_two_sorted_lists:

  - We check the Node being non Empty while traversing, again.
  -
  - Make a dummy node to simplify the merging logic.

- 037.reorder_list:

  - Two phases:
  -
  - Find second portion of the linked list, reverse it
  - add it one by one
  -
  - To find the middle of the LL, use a slow and fast pointer
  -
  - slow pointer at first node, fast pointer at second node
  -
  - keep going until fast pointer reaches None or last element
  -
  - if it is an even list, slow pointer will be the
  - last element of the first portion
  -
  - if it is an odd list slow pointer will
  - be in the middle exactly
  -
  - we need pointer at the beginning of each first and second lists
  -
  - for the last node of the first list, node.next should be None 
 
- 038.remove_nth_node_from_end_of_list:

  - Like a lot of LL questions, lets use two pointers
  -
  - 1 2 3 4 5  n = 2  - how can we identify 4 is the second to last element ?
  -
  - Lets initialize left pointer at the beginning of the list
  - and move right pointer n times (it will start at 3)
  -
  - this way the space between two pointers will be exactlY
  - when right pointer reaches None, left pointer will be at 4
  -
  - but because we want to delete 4, we need Left pointer to be at
  - so lets add a dummy node at the beginning
 
- 039.copy_list_with_random_pointer:

  - we can just copy nodes but we cannot just make a random index for
  - future nodes that we have not made yet
  -
  - Because of this, make 2 passes
  -
  - 1) at first pass just make copies of the nodes and a hashmap
  -
  - 2) at second pass, pointer connections and random values, using the hashmap


- 040.sliding_window_maximum:

  - I was stuck in thinking the inequality of sizes for LL's. Turns out you can
  - just add 0 nodes to the one that is missing.
  -
  - My approch would work, but its not why the question is asked.
  -
  - Do not forget about trying to understand the question. Calm in the first 3 minutes.
  -
  - we check if the node is None for traversing the LinkedList.
  -
  - In addition, we have a simple condition for the sum called "CARRY"


- 041.linked_list_cycle:

  - We are trying to understand if the traversal of
  - the LL is an infinite loop
  -
  - If there is a cycle in it, it should be infinite
  -
  - BUt the most precise way is to check whether we
  - pass through some arbitrary node, twice
  -
  - Lets use slow and fast pointers. Floyd's Tortoise and Hare
  -
  - if fast pointer catches slow pointer, there has to be a cycle
  -
  - Just a reminder, you can use a hashset for this question


- 042.find_the_duplicate_number:

  - You can use a dict but it wont cut it, because it wont be o(1) time
  -
  - It is pretty incredible but this is a Linked List question
  - [1,3,4,2,2] has length of 5 and the values has to
  - be between 1 - 4
  -
  - these are not values, these are pointers
  -
  - i =  0  1  2  3  4
  - n =  1  3  4  2  2
  -
  - If there are a node which is pointed by more than 1 node
  - we solve the problem
  - 
  - after you find the first intersection of slow and fast pointers
  - start a new slow pointer from the beginning, when
  - it meets the old slow pointer, you found your solution


- 043.lru_cache:

  - We will have a capacity
  -
  - we will have a doubly linked list, also a hash map
  - with keys and values as pointers to nodes.
  -
  - LRU and most recent will be pointed and updated.
  - So we need two pointers just for those. Which will be Nodes as well.
  -
  - You can also use Queues, implemented with Python lists

- 044.merge_k_sorted_lists:

  - My initial solution was to use a simple list and
  - get every element in it, sort it and make a new LL
  -
  - The problem is about Merge Sort
  - simply merge two lists until you have merged them all.
  - 
  - For merging two lists, you can use a helper function
  -
  - ** do not forget edge cases ** 

- 045.reverse_nodes_in_k_group:

  -   Start with a dummy node and sets it as the
  - previous node for the first group.
  - This dummy node simplifies the code for handling
  - the head of the list and avoids edge cases.
  -
  - You can write a simple helper function to get the kth node
  -
  - It then identifies the next group by accessing
  - the node immediately following the kth node.
  -
  - The core part of the code is the loop that reverses
  - the k nodes in the current group. It uses two
  - pointers (prev and current) to reverse the direction
  - of the next pointers for the k nodes.
  -
  - This effectively reverses the group.
  -
  - After reversing the group, it updates the pointers to link
  - the reversed group to the previous group. It also sets
  - group_prev to the previous group's end, which prepares
  - it for the next iteration.


## Trees

- 046.invert_binary_tree:

  - We can approach the problem with recursion
  -
  - Simply make the swap and call the method on to the children Node
  -
  - Depth-First Search (DFS) in the context of a binary tree. DFS is
  - a common algorithm used for traversing or searching tree and
  - graph data structures. In this specific case, it's a pre-order
  - DFS because it visits the current node, then recursively explores
  - its left and right subtrees.

- 047.maximum_depth_of_binary_tree:

  - My natural approach was to just recursive DFS
  -
  - 3 ways to solve it: Recursive DFS, Iterative DFS and Breadth-First Search
  -
  - Recursively calculate the depth and return the maximum among them
  -
  - If you want no recursion, BFS is cool. You can use a queue to hol the nodes
  - and increase depth on each level

- 048.diameter_of_binary_tree:

  - The diameter can pass through the node or not.
  -
  - For that, we need a depth calculation for the possible
  - root passing solution
  -
  - We also need to calculate the diameter of the left and right
  - subtrees, becuase it may be the case that max diameter is
  - never passing through the root node

- 049.balanced_binary_tree:

  - We can do a recursive DFS on subtrees and compare the results
  - This will be o(n) * n
  -
  - We can use the heights of the subtrees and return a boolean
  - based on not expecting a node height
  -
  - ``` return height != -1```
  -
  - We can do better than starting from root node and asking
  - the question is the subtree balanced ? again and again
  -
  - Just define a recursive dfs but alongside balance, return the
  - height too

- 050.same_tree:

  - My approach was to traverse the tree and add all elements together
  -
  - We can use DFS -
  - with time complexity o(p+q) - all elements in both trees
  -
  - Make a recursive call on the children of the node
  - you are working on
 
- 051.subtree_of_another_tree:

  - The brute force algorithm will o(s *t)
  -
  - But most tree problems are easier when we think recursively.
  -
  - However, do not forget the edge cases.
  -
  - We basically just write the same_tree method and use it
  - in our is_subtree method
 
- 052.lowest_common_ancestor_of_binary_tree:
 
  - Its a binary search tree so the values are really useful.
  -
  - If both of the values are smaller than root.vaL
  - go to left subtree
  -
  - if both of the values are larger than root.val
  - go to right subtree
  -
  - if one is bigger and one is smaller than root.vaL
  - the anchestor will be the split happens in the tree
  - the LCA is found, so to speak
  -
  - If we bump into the node, starting from the the root
  - that is the LCA because nothing below will be
  - the common ancestor
  -
  - time complexity is the height of the tree, o(log n)
  - because we are only visiting single node at each level
  -
  - We can also approach the question recursively

- 053.binary_tree_level_order_traversal:
  
  - use breadth-first search. We use queues for that.
  -
  - Initialize the queue with the root node
  -
  - For each level, make a list of nodes
  - move on to (possibly) existing child nodes

- 054.binary_tree_right_side_view:

  - Only going right won't work
  -
  - The nodes on the left subtree can still have some right nodes
  - that should have been taken into account
  -
  - We can use Breadth First Search - Level Ordering Traversal
  -
  - At each level, we will be searching for the right most node
  -
  - Loop through all the nodes at the current level.
  - For each node, remove it from the left end of
  - the deque (q) using q.popleft().
  -
  - If the node is not None, update right_side to
  - the current node. This is because you are traversing
  - from left to right within the level, so the rightmost
  - node encountered will be the last one
  - assigned to right_side. 

- 055.count_good_nodes_in_binary_tree:

  - YOu dont have to pass the whole path to the lower level
  - you just need to pass the max value
  -
  - We can use preorder traversal (dfs)
  -
  - Root is always a good node and root is equal to root

- 056.validate_binary_search_tree:

  - you can think "this is dfs, just check neighbors"
  - that does not cut it.

  -    3           5         4  7  8
  -
  - the 4 in the tree is not recogniziable just with checking neighbors
  -
  - as we go down the tree, we need to update boundaries
  -
  - as we go to left, we need to update right boundary
  - as we go to right, we need to update left boundary
  -
  - so that we have a binary search tree   

- 057.kth_smallest_element_in_a_bst:

  - We can make a recursive in order traversal and
  - append all elements from smallest to kth smallest
  - on a temporary list
  -
  - OR
  -
  - lets use a stack and solve the question iteratively
  - this is also in order traversal
  -
  - make a stack
  - add every node onto the stack until you get to
  - where node.left is None
  - when you get that case, that is your leftmost element.
  - pop it from the stack, check if it has a node.right
  - than go one level up
  -
  - when stack is empty, return
  - number of elements visited
  - once this is equal to k, return

- 058.construct_binary_tree_from_preorder_and_inorder_traversal:

  - Reminder on traversals:
  -
  - preorder traversal
  - starts from root, and its just like reading
  -
  - inorder traversal
  - slide from left to right
  -
  - after from seperating the root from preorder traversal
  - we will use inorder traversal tom determine
  - which of the nodes should be in the right subtree and
  - which should be in the left subtree
  -
  - in order
  - it will give us for every node
  - which nodes are on its left and which are on its right
  -
  - the left subtree is where we start from 1 in preorder until mid
  - and left side in inorder traversal
  - ``` root.left = self.buildTree(preorder[1 : mid+1], inorder[:mid]) ```
  - the right subtree is where we start from mid + 1 in preorder until end
  - and right side in inorder traversal
  - ``` root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) ```  

- 059.binary_tree_maximum_path_sum:

  - negative values can be included in a max path
  - just think -1
  -
  - to make a path, we need to choose between 2 options.
  - we cannot go everywhere like a euler tour
  -
  - we will use dfs and starting from subtrees
  - we will return the maximum value to parent
  - without splitting
  -
  - an edge case is for negative valued children
  - we can choose not to include the children by using
  - max(left, right, 0) 

- 060.serialize_and_deserialize_binary_tree:

  - You can solve the problem with breadth-first search
  - or you can solve it with depth first search
  - using preorder traversal
  -
  - for the example tree
  -    1
  -   / \
  -  2   3
  -     / \
  -    4   5
  -
  - "1,2,N,N,3,4,N,N,5,N,N"
  - is the resulting string
  - if we used N for None nodes
  -
  - For each subtree, check the left and right nodes,
  - and recursively go a level up
  -
  - Also added the Breadth First Search Solution

## Tries

- 061.implement_trie_prefix_tree:
 
  - We can start with making a TrieNode for the class.
  - Each node will have child nodes, and at each word ending
  - we will have a Flag indicating the end.
  -
  - Using a Trie data structure, we have efficient
  - string search and prefix matching.
  -
  - The time complexity for inserting, searching, and
  - checking prefixes in a Trie is O(L), where L is the length
  - of the word or prefix, making it an efficient choice
  - for string-related tasks.
  -
  - For different words we will be using a lot of the same nodes
  -
  - .
  -  \
  -   a
  -     \ 
  -      p 
  -        \
  -         p 
  -        / \ 
  -       e   l 
  -     /      \ 
  -    n        e

- 062.design_add_and_search_words_data_structure:

  - This is obviously a Trie (Prefix Tree) Question
  -
  - Because we are looking for all words starting
  - with some characters "ab." or "b.."
  -
  - A root and 26 children in the Trie
  -
  - "." character is a wildcard. It can be used instead any character
  - We should use end of the word to show that word ended
  -
  - The Trie solution gives us time limit exceeded
  -
  - SO a hashmap solution is added.
 
- 063.word_search_2:

  - we need to make a data structure where
  - we can see every possible word in the board
  - can use a Trie
  -
  - Brute force would be,
  - starting from each tile, run a depth first search
  - and check if you can make the words
  -
  - we can check every word at the same time
  - because our main condition is based on prefix
  - So a Trie is great!
  -
  - lets make a Trie for our words
  - in order to not check the words list every time
  - we go down in out dfs
  - Also we do not have to check tiles that our words
  - does not start with.
  -
  - Base case for the DFS is pretty big:
  -
  - out of bounds
  - already visited position
  - maybe the character we are working
  - on is not in out Trie 

## Backtracking

- 064.subsets:

  - The backtracking algorithm enumerates a set of partial candidates
  - that, in principle, could be completed in various ways to give all
  - the possible solutions to the given problem. The completion is done
  - incrementally, by a sequence of candidate extension steps.
  -
  - Conceptually, the partial candidates are represented as the nodes
  - of a tree structure, the potential search tree. Each partial
  - candidate is the parent of the candidates that differ from it
  - by a single extension step; the leaves of the tree are the partial
  - candidates that cannot be extended any further.
  -
  - The backtracking algorithm traverses this search tree recursively, from
  - the root down, in depth-first order. At each node c, the algorithm checks
  - whether c can be completed to a valid solution. If it cannot,
  - the whole sub-tree rooted at c is skipped (pruned). Otherwise, the
  - algorithm (1) checks whether c itself is a valid solution, and if
  - so reports it to the user; and (2) recursively enumerates all sub-trees
  - of c. The two tests and the children of each node are defined
  - by user-given procedures.
  -
  - Therefore, the actual search tree that is traversed by the
  - algorithm is only a part of the potential tree. The total cost
  - of the algorithm is the number of nodes of the actual tree
  - times the cost of obtaining and processing each node. This fact
  - should be considered when choosing the potential search tree
  - and implementing the pruning test.
  -
  - When applying backtracking to a problem, you can make a decision
  - tree to represent the sequence of choices made and the paths
  - explored to reach a solution.
  -
  - Backtracking Process: As backtracking proceeds, it explores different
  - branches, and when it reaches a dead-end (a choice that doesn't
  - lead to a solution), it backtracks to a previous decision point
  - and explores a different branch. This process is similar
  - to traversing decision trees.
  -
  - We can make a decision tree to represent the question
  -
  - We have the choice of adding or not adding
  - every element for the subset
  -
  - For every level of the dfs, we will decide on the condition
  - we are moving on and will call dfs again on one level deeper.
  -
  - Stop when we reach the leafs for the decision tree


- 065.combination_sum:

  - The simple approach would be make a hudge decision tree.
  -
  - The problem with that approach is that we will not be able
  - to identify duplicates
  -
  - to solve the decision tree
  - we approach it in a unique manner
  - at every level, when we decide that we are not adding
  - a value to a possible solution, we wont
  - be adding that value anymore
  -
  - to track which elements we can choose
  - we will have a pointer and after each decision we
  - will move the pointer
  -
  - In backtracking, we have a decision to be made in the
  - end of dfs function
  - 

- 066.permutations:

  - There is itertools for permutation and combination
  -
  - You can use a stack with recursion
  -
  - You can use backtracking, thinking with a decision tree
  -
  - pop an element and call permute again on the smaller sequence
  -
  - before returning to the beginning of the loop,
  - append back the element you popped
  - This way, you'll traverse the sequence exactly how you want. 

- 067.subsets_2:
  
  - Use backtracking, because we can see the solution is
  - about a decision tree
  -
  - Sort the list so that you can compare consecutive elements
  -
  - for every decision, either select or do not select element
  - to be in the subset
  -
  - before going to not including part, move your pointer to
  - escape duplicates
  -
  - and even before that, pop the last element you
  - added to current subset

- 068.combination_sum_2:

  - for every element, we can include it or not include it
  - time complexity will be 2^n
  -
  - if we just brute force it
  - there will be duplicate solutions
  -
  - to get rid of duplicate solutions
  - subtract the element from the target and
  - make sure the left subtree is including the unique
  - element and right subtree is not
  -
  - this was we will make sure that the results will be unique
  - [10, 1, 2, 7, 6, 1]
  - sort it
  - [1, 1, 2, 6, 7, 10]
  -
  - for each subtree either add or not add the element
  - move the pointer accordingly

- 069.word_search:

- 070:

- 071:

- 072:

## Heap / Priority Queue

- 073.kth_largest_element_in_a_stream:

  - if we use an array,
  - sorting would be n log n
  - finding where to insert would be o(n)
  -
  - lets use a min heap of size k
  - we can get the min of min heap in o(1)
  - we can add an element in log n time
  -
  - kth element will be the smallest element in
  - size k min heap

- 074.last_stone_weight:

  - if we use a sorted approach, we have to sort
  - the list every time
  -
  - use a max heap,
  - heapify takes o(n)
  - every time accessing max heap is o(log n) - possibly
  - running n times
  -
  - to make a max heap in Python, just multiply
  - every value with -1
  -
  - in the calculations, use the example in your mind.    
