class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        out = []
        carry = 1

        while i >= 0:
            d = digits[i]
            d += carry
            if d > 9:
                d = 0
            else:
                carry = 0
            out.insert(0, d)
            i -= 1
        
        if carry == 1:
            out.insert(0, carry)
        
        return out