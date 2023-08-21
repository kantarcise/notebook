# [The Perfect Hour.](https://youtu.be/WkfkMTEqQak?t=904)

## Arrays & Hashing

- containsDuplicate:
  - You can use a hash map and get the maxOccurance from values. (freq dict , ***max_occurance = max(freq.values()***)
  -
  - CAREFUL - ***max (dict , key=dict.get())*** WILL GIVE YOU THE KEY not the VALUE
  -
  - You can use greedy approach and exit as soon as you find something occuring twice.
  -
  - You can use sets, which has ***add()*** and ***remove()*** methods.
 
- isAnagram:
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

- twoSum:
  - Basic idea is to use elements and find the remainder from the target.
  -
  - ***index()*** can be used with a START index to find the (possibly) second element - terrible complexity o(n)
  - 
  - You can use a hashmap, for elements and their indexes.
  - 
  - Never forget: ***for index, elem in enumerate(sequence)***
