"""
Design an algorithm to encode a list of strings to a string.

The encoded string is then sent over the network and is 
decoded back to the original list of strings.

Implement encode and decode.

Example 1:

    Input: ["lint","code","love","you"]
    Output: ["lint","code","love","you"]

    Explanation:

        One possible encode method is: "lint:;code:;love:;you"


Example 2:

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

    # MY FIRST TRY
    
    def encode(self, strs: list) -> str:
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        return "~".join(strs)


    def decode(self, str: str) -> list:
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
        # write your code here
        return str.split("~")


    def encode_stateless(self, strs: list) -> str:
        result = ""

        for elem in strs:
            # this is not ideal because strings are 
            # immutable
            # we are making a lot of objects in this loop
            result += str(len(elem)) + "#" + elem

        return result

    def decode_stateless(self, input_string: str) -> list:
        # we will populate this result list
        result = []
        # string starting index
        i = 0
        
        # until you are end of the string
        while i < len(input_string):
            # this index holds width for the length of the word
            j = i
            while input_string[j] != "#":
                j += 1
            
            length = int(input_string[i:j])
            result.append(input_string[j+1: j+1+length])
            
            # move index
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
