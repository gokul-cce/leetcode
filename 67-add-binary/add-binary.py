class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binary(num):
            total = 0
            index = 0
            for i in range(len(num)-1,-1,-1):
                if num[i] == '1':
                    total += int(num[i]) * (2**(index))
                index += 1
            return total
        res = binary(a) + binary(b)
        return str(bin(res))[2:]