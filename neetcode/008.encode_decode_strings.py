"""
Description

Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is 
decoded back to the original list of strings.

Please implement encode and decode

Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]

Explanation:

One possible encode method is: "lint:;code:;love:;you"


Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]

Explanation:
One possible encode method is: "we:;say:;:::;yes"


Takeaway:

THe description is not really complete.

We are trying to encode decode stateless. So we somehow need to 
clarify the word lenghts while we are trasporting them.

for that we can use the lenght of the words and sent them prior
to the encoded words.

When we are decoding, we will know how many indexes we need to be 
looking for, simply using the length.

"""

class Solution:

    # MY FIRST TRIAL
    def encode(self, strs):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        return "~".join(strs)


    def decode(self, str):
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
        # write your code here
        return str.split("~")


    def encode_stateless(self, strs):
        result = ""

        for elem in strs:
            result += str(len(elem)) + "#" + elem

        return result

    def decode_stateless(self, str):
        result = []
        i = 0

        while i < len(str):
            # this index holds width for the length of the word
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            result.append(str[j+1: j+1+length])
            i = j + 1 + length
        return result



if __name__ == "__main__":
    sol = Solution()

    list_of_strings = ["lint","code","love","you"]
    encoded = sol.encode(list_of_strings)
    decoded = sol.decode(encoded)
    print(f"Original list {list_of_strings}, after process {decoded}")

    print("\nCool solution:\n")


    encoded_stateless = sol.encode_stateless(list_of_strings)
    decoded_stateless = sol.decode_stateless(encoded_stateless)
    print(f"Original list {list_of_strings}, after process {decoded}")