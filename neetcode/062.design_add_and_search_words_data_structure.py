"""
Design a data structure that supports adding new words and finding 
if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary(): Initializes the object.

    void addWord(word): Adds word to the data structure, it 
    can be matched later.

    bool search(word): Returns true if there is any string in the 
    data structure that matches word or false otherwise. 
    word may contain dots '.' where dots can be matched
    with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:

    1 <= word.length <= 25
    word in addWord consists of lowercase English letters.
    word in search consist of '.' or lowercase English letters.
    There will be at most 2 dots in word for search queries.
    At most 104 calls will be made to addWord and search.

Takeaway:

This is obviously a Trie (Prefix Tree) Question

Because we are looking for all words starting 
with some characters "ab." or "b.."

A root and 26 children in the Trie

"." character is a wildcard. It can be used instead any character
We should use end of the word to show that word ended

The Trie solution gives us time limit exceeded

SO a hashmap solution is added.

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_ends = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            # go on to the next character
            current = current.children[char]
        # last character saying the word ended
        current.word_ends = True
        
    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            current = self.root

            for i in range(len(word)):
                c = word[i]

            if c == ".":
                for child in current.children.values():
                    if dfs(i + 1, child):
                        # we found a match
                        return True
                return False

            else:
                if c not in current.children:
                    return False
                # onto next
                current = current.children[c]
            # if we have no "." in the word
            return current.word_ends
        return dfs(0, self.root)


class WordDictionary:

    def __init__(self):
        # Initialize the WordDictionary with an empty root node,
        # which is represented as a dictionary.
        self.root = {}

    def addWord(self, word: str) -> None:
        # Add a word to the WordDictionary.
        # Traverse the WordDictionary's tree structure, creating
        # nodes for each character in the word.
        # Mark the end of a word with the '*' key in the dictionary.
        curr_node = self.root
        for ch in word:
            if ch not in curr_node:
                curr_node[ch] = {}
            curr_node = curr_node[ch]
        curr_node['*'] = False

    def search(self, word: str) -> bool:
        # Search for a word in the WordDictionary.
        # Use a depth-first search (DFS) approach to traverse
        # the tree and match characters in the word.
        def dfs(node, index):
            if not node:
                # If we reach a null node, the word cannot be found.
                return False
            if index == len(word):
                # If we have reached the end of the word,
                # check if the '*' key exists to indicate a complete word.
                return '*' in node
            if word[index] != '.':
                if word[index] not in node:
                    # If the character in the word is not in the tree,
                    # the word cannot be found.
                    return False
                # Continue searching for the next character in the word.
                return dfs(node[word[index]], index + 1)
            for n in node.values():
                # If the character is a dot ('.'), explore all possible
                # branches and check if any path leads to a valid word.
                if dfs(n, index + 1):
                    return True
            return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)