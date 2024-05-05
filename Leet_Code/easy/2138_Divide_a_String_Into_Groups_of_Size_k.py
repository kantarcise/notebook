"""
A string s can be partitioned into groups of 
size k using the following procedure:

The first group consists of the first k characters 
of the string, the second group consists of the next 
k characters of the string, and so on. 

Each character can be a part of exactly one group.

For the last group, if the string does not have k 
characters remaining, a character fill is used to 
complete the group.

Note that the partition is done so that after 
removing the fill character from the last group (if 
it exists) and concatenating all the groups in order, 
the resultant string should be s.

Given the string s, the size of each group k and the 
character fill, return a string array denoting the 
composition of every group s has been divided 
into, using the above procedure.

Example 1:

    Input: s = "abcdefghi", k = 3, fill = "x"

    Output: ["abc","def","ghi"]

    Explanation:
        
        The first 3 characters "abc" form the first group.
        The next 3 characters "def" form the second group.
        The last 3 characters "ghi" form the third group.
        Since all groups can be completely filled by characters 
            from the string, we do not need to use fill.
        Thus, the groups formed are "abc", "def", and "ghi".

Example 2:

    Input: s = "abcdefghij", k = 3, fill = "x"
    
    Output: ["abc","def","ghi","jxx"]

    Explanation:
    
        Similar to the previous example, we are forming the 
            first three groups "abc", "def", and "ghi".
        For the last group, we can only use the character 'j' 
            from the string. To complete this group, we add 'x' twice.
        Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".

Constraints:

    1 <= s.length <= 100

    s consists of lowercase English letters only.

    1 <= k <= 100
    
    fill is a lowercase English letter.

Takeaway:

    Grouping can be done with while and for loops.

    for loops are able to take bigger steps!
"""
class Solution:
    def divideString__(self, s: str, k: int, fill: str) -> List[str]:
        # this works,
        # can I make it faster ?
        
        # k characters each
        # fill character
        
        # k is our slicing
        # make a result list
        # iterate over s
        # when got to k, append to result
        
        # careful! - off by one error
        # fill with fill
        
        res = []
        l, r = 0, 1
        while r < len(s):
            if r % k == 0:
                res.append(s[l:r])
                l = r
            r += 1
        
        # off by one
        res.append(s[l:r])
        
        # print(res)
        
        if len(res[-1]) == k:
            return res
        else:
            res[-1] += (k - len(res[-1])) * fill
            return res
        
    def divideString_(self, s: str, k: int, fill: str) -> List[str]:
        # still not fast
        res, temp = [], []
        
        for c in s:
            temp.append(c)
            
            if len(temp) == k:
                res.append("".join(temp))
                temp = []
            
        # off by one
        if temp: 
            res.append(temp)
        
        # add fills if needed
        if len(res[-1]) != k:
            while len(res[-1]) != k:
                res[-1].append(fill)
            print(res[-1])
            
            res[-1] = "".join(res[-1])

        return res

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # a way to calculate the iteration faster
        # is to have a smaller iteration
        res=[]

        # stepping in range
        for i in range(0,len(s),k):
            res.append(s[i:i+k])

        last=res[-1]
        # fill the last element
        while len(last) != k :
            last=last+fill
        
        # pop old last element
        # and append the filled one
        res.pop(-1)
        res.append(last)

        return res
