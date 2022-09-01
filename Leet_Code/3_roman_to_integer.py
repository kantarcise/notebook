class Solution:
    def romanToInt(self, s: str) -> int:
        _total = 0
        # dictionary for roman numerals
        val_map = {"0": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # Adding a special "0" character to the end of every input,  so that we iterate from index 1:n and look back at the previous character.
        s += "0"
        for i in range(1,len(s)):
            v = val_map[s[i-1]]
            if val_map[s[i]] > v:
                _total -= v
            else:
                _total += v
        return _total   
