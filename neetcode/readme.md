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
