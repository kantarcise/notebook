"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.

bool insert(int val) Inserts an item val into the set if not present. Returns 
true if the item was not present, false otherwise.

bool remove(int val) Removes an item val from the set if present. Returns 
true if the item was present, false otherwise.

int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.

You must implement the functions of the class such that each function 
works in average O(1) time complexity.

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

Takeaway:

This was really good exercise as for set, dict, list workout.

random.choice(iterable) is a classic

Based on conditions, we might need more than 1 data structure.

Cannot access elements in set in o(1) time. 

There is no slicing or getitem for sets.

"""
from random import randint

class RandomizedSet_:
    """ Using set.pop() will not work because this changed after
    Python 3.6 , as sets became ordered.
    Two cool methods:
    
    set.remove(element) - will return element and if it does not 
        exist will throw exception
    
    set.discard(element) - will return element and if it does not
        exist, no exceptions. (kinda like str.find())
    
    Let's use a list instead
    
    This was a failure, we need more than 1 data 
    structure to solve this problem.
    
    The SMART solution is down below
    """
    def __init__(self):
        self.container = []

    def insert(self, val: int) -> bool:
        if val not in self.container:
            self.container.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        # _rand_index = randint(0, len(self.set))
        # _element = self.set[_rand_index]
        # self.set.remove(_element)
        # return _element
        # THIS IS WRONG
        return self.set.pop()
        
import random

class RandomizedSet:

    def __init__(self):
        self.seq = []
        # for o(1) access
        # {element: index}
        self.map = {}

    def insert(self, val):
        if val in self.map:
            return False
        
        # o(1)
        self.seq.append(val)
        # set the index of the new element
        self.map[val] = len(self.seq) - 1
        return True

    def remove(self, val):
        if not val in self.map:
            return False
        # 10, 20, 30
        # remove 10

        # index is 0
        index = self.map[val]
        
        # set the to be removed element
        # as the last element of list
        self.seq[index] = self.seq[-1]
        
        # set new index for the last element
        self.map[self.seq[-1]] = index
        
        # remove from list
        self.seq.pop()
        # remove from dict
        del self.map[val]
        
        return True

    def getRandom(self):
        return random.choice(self.seq)     
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
