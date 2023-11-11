# my first approach
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        
        j = 1
        for i in range(len(columnTitle)-1, -1, -1):
            # result = ord(f"{columnTitle[i].lower()}") * j
            result += (ord(columnTitle[i].lower()) - ord('a') + 1) * j
            j *= 26
            
        return result

# fast and clean
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        out = 0
        for i, x in enumerate(columnTitle[::-1]):
            out += (ord(x) - 64) * 26**i

        return out
