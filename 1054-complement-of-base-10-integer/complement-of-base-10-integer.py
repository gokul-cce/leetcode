class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = ''
        if n == 0:
            return 1
        while n:
            remainder = n % 2
            if remainder == 0:
                binary = '1' + binary
            else:
                binary = '0' + binary
            n //= 2
        print(binary)
        n = len(binary)
        complement = 0
        for i in range(n-1,-1,-1):
            complement += int(binary[i]) * (2**(n-(i+1)))
        return complement
        