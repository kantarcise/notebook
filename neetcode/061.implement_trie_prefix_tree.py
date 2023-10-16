# TODO

"""
Trie - Prefix Tree

A trie (pronounced as "try") or prefix tree is a tree data 
structure used to efficiently store and retrieve keys in a 
dataset of strings. There are various applications of this 
data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie(): Initializes the trie object.

void insert(String word): Inserts the string word into the trie.

boolean search(String word): Returns true if the string 
word is in the trie (i.e., was inserted before), and 
false otherwise. 

boolean startsWith(String prefix): Returns true if there 
is a previously inserted string word that has the 
prefix prefix, and false otherwise.
 
Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output
[null, null, true, false, true, null, true]

Explanation

Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 
Constraints:

1 <= word.length, prefix.length <= 2000
Word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

Takeaway:

We can start with making a TrieNode for the class.
Each node will have child nodes, and at each word ending 
we will have a Flag indicating the end.

Using a Trie data structure, we have efficient 
string search and prefix matching.

The time complexity for inserting, searching, and 
checking prefixes in a Trie is O(L), where L is the length 
of the word or prefix, making it an efficient choice 
for string-related tasks.

For different words we will be using a lot of the same nodes

.
 \ 
  a
   \ 
    p 
     \
      p 
     / \ 
    e   l 
   /      \ 
  n        e

"""

class TrieNode:
    def __init__(self):
        self.children = {}  # A dictionary to store child nodes.
        self.is_end_of_word = False  # A flag to indicate the end of a word.

class Trie:

    def __init__(self):
        # root is a TrieNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word in the Trie
        
        Start at the root node.
        For each character in the word:
        Check if the character is a child of the current node.
        If not, create a new node for the character.
        Move to the child node corresponding to the character.
        After processing all characters, mark the 
        last node as the end of a word."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            # to the next node
            current = current.children[char]
        # word is over after word ends.
        # ending node should have is "is_end_of_word" attribute set to True
        current.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        """
        Search for a node

        Start at the root node.
        For each character in the word:
        Check if the character is a child of the current node. 
        If not, the word is not in the Trie.
        Move to the child node corresponding to the character.
        After processing all characters, check if the last node 
        is marked as the end of a word."""
        current = self.root
        for char in word:
            if char not in current.children:
                # if no complete match, return False
                return False
            # to the next node
            current = current.children[char]
        # if the word is not ended, return False
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Check if a node starts with a given prefix

        Start at the root node.
        For each character in the prefix:
        Check if the character is a child of the current node. 
        If not, there are no words with the given prefix.
        Move to the child node corresponding to the character.
        After processing all characters, the prefix exists if 
        the search doesn't indicate the end of a word."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            # on to the next node
            current = current.children[char]
        # if we made it this far, word starts with the given prefix
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)