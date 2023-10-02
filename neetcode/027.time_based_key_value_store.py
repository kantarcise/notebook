"""

Design a time-based key-value data structure that can store multiple values
 for the same key at different time stamps and retrieve the key's value
at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.

void set(String key, String value, int timestamp) Stores the key 'key' with the
 value 'value' at the given time timestamp.

String get(String key, int timestamp) Returns a value such that set was called
 previously, with timestamp_prev <= timestamp. If there are multiple such
  values, it returns the value associated with the largest timestamp_prev.
   If there are no values, it returns "".
 
Example 1:

Input

["TimeMap", "set", "get", "get", "set", "get", "get"]

[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

Output

[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation

TimeMap timeMap = new TimeMap();

timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" 
along with timestamp = 1.

timeMap.get("foo", 1);         // return "bar"

timeMap.get("foo", 3);         // return "bar", since there is no value 
corresponding to foo at timestamp 3 and timestamp 2, then the only value 
is at timestamp 1 is "bar".

timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along
 with timestamp = 4.

timeMap.get("foo", 4);         // return "bar2"

timeMap.get("foo", 5);         // return "bar2"
 

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.

Takeaway:


"""

# my first try - not complete - not true
class TimeMap_:

    def __init__(self):
        # key is a string
        # value is a list of value and timestamp
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.map:
            self.map[key].append([value, timestamp])
            return
        else:
            self.map[key] = []
            self.map[key].append([value, timestamp])
            return

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            # return the highest timestamp value
            result_list = self.map.get(key)
            difference = map (lambda a : timestamp - a, [elem[1] for elem in result_list])
            # find index of min difference
            # return that element from the result_list
        else:
            return
 

class TimeMap:
    """The idea of yourself is not bad.
    But for get method you can use the fact that timestamps are strictly increasing
    If that was not the case, you would have to sort the list of timestamps for each get"""


    def __init__(self):
        # key is a string
        # value is a list of value and timestamp
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []

        self.map[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        result = ""

        values = self.map.get(key, [])

        #binary search
        l, r = 0 , len(values) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if values[m][1] <= timestamp:
                # closest we have seen so far
                result = values[m][0]
                # search to the left of the sequence
                l = m + 1
            else:
                r = m - 1

        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


if __name__ == "__main__":
    obj = TimeMap()
    obj.set(key,value,timestamp)
    param_2 = obj.get(key,timestamp)