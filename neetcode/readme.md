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
  
  - Here is something interesting

  - a,b,c,d,*e, f  = range(10)

  - # a = 0
  - # b = 1
  - # c = 2
  - # d = 3
  - # e = [4,5,6,7,8]
  - # f = 9
 
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

  - Takeaway: enumerate is still one of the best ways to traverse a sequence.
  -
  - YOu can and you should use dictinaries whenever you want to store and access a value/key combination.
 
- 012.3Sum:
  
  - Takeaway:  Two pointer approach is simple. you define them and you set up conditions on their changes.
  - 
  - Updating a sequence on the fly is NOT HELPFUL so far. No Removes no copying lists  please.
  -
  - Solid effort on compartmentalizing. Defining the object which you are thinking to return is a good and simple idea.

- 013.containerwithmostwater:

  - Takeaway:
  - 
  - Brute Force can help you find a pattern in which you can expand on.
  - 
  - Two pointers keep being the same, define them first and on condition
 increase/ decrease them.

- 014.trapping_rain_water:

  - Takeaway:
  - 
  - two pointers are still doing wonders.
  -
  - trying to find a pattern for each step is the key for approaching these problems.
  -
  - you need to be calm. you will be calm when you solve your 250th question.
  -
  - just a numbers game

- 015.valid_paranthesis:

  - Takeaway:
  - 
  - matching symbols is just asking for a hash map to be used
  - 
  - we are using a stack for storing all of the opening brackets.
  - 
  - For each closing bracket we are looking for the last element 
  - in stack to be matched by the closing symbol
  - 
  - if everything went smooth, stack should be empty in the end.
