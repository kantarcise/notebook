"""
Reverse bits of a given 32 bits unsigned integer.

Note:

    Note that in some languages, such as Java, there is no unsigned integer 
    type. In this case, both input and output will be given as a signed 
    integer type. 
    
    They should not affect your implementation, as the 
    integer's internal binary representation is the same, whether it 
    is signed or unsigned.

    In Java, the compiler represents the signed integers using 2's 
    complement notation. 
    
    Therefore, in Example 2 above, the input represents 
    the signed integer -3 and the output represents the signed 
    integer -1073741825.

Example 1:

    Input: n = 00000010100101000001111010011100
    
    Output:    964176192 (00111001011110000010100101000000)
    
    Explanation: 
    
        The input binary string 00000010100101000001111010011100 represents 
        the unsigned integer 43261596, so return 964176192 which its binary 
        representation is 00111001011110000010100101000000.

Example 2:

    Input: n = 11111111111111111111111111111101
    
    Output:   3221225471 (10111111111111111111111111111111)
    
    Explanation: 
    
        The input binary string 11111111111111111111111111111101 
        represents the unsigned integer 4294967293, so return 3221225471 which 
        its binary representation is 10111111111111111111111111111111.
 
Constraints:

    The input must be a binary string of length 32

Takeaway:

    AND ing with 1 will give the value of the element

    we can shift it to get the next bits.

    pretty cool that you can solve it with strings too.

    ljust() ! -> left justified ??
"""

class Solution:
    def reverseBits__(self, n: int) -> int:
        # this was my first approach,
        # did not work 
        
        # but we remembered:
        # bin returns string. it has "0b" leading.
        # using lists is not necessary.

        result = []
        for elem in bin(n)[2:]:
            result.append(elem)
        return int("".join(result[::-1]), 2)
    
    def reverseBits_(self, n: int) -> int:
        # pretty cool that you can do that with strings.

        # ljust() !

        # Convert the integer to its binary representation and remove the '0b' prefix
        binary_representation = bin(n)[2:]

        # Reverse the binary string and pad with leading zeros if necessary
        reversed_binary = binary_representation[::-1].ljust(32, '0')

        # Convert the reversed binary string back to an integer
        return int(reversed_binary, 2)

    def reverseBits(self, n: int) -> int:
        # Initialize result to 0
        result = 0
        
        # Iterate over each bit position (32 bits for a 32-bit integer)
        for _ in range(32):
            # Shift the bits in 'result' to the left by 1 position
            result = (result << 1)
            
            # Set the rightmost bit of 'result' to the current rightmost bit of 'n'
            result |= (n & 1)
            
            # Right shift 'n' to move to the next bit
            n >>= 1
        
        # The reversed integer
        return result
