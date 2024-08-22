# class Solution:
#     def findComplement(self, num: int) -> int:
#         binary_rep = format(num, '03b')
#         complement = ''.join('1' if bit == '0' else '0' for bit in binary_rep)
#         decimal_of_complement = int(complement, 2)
#         return decimal_of_complement 



class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: Convert the number to binary representation without the '0b' prefix
        binary_rep = format(num, 'b')
        
        # Step 2: Flip each bit to find the complement
        complement = ''.join('1' if bit == '0' else '0' for bit in binary_rep)
        
        # Step 3: Convert the binary complement back to a decimal integer
        decimal_of_complement = int(complement, 2)
        
        return decimal_of_complement
