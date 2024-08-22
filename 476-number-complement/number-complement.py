class Solution:
    def findComplement(self, num: int) -> int:
        binary = ''
        while num:
            remainder = num % 2
            if remainder == 0:
                binary = '1' + binary
            else:
                binary = '0' + binary
            num = num // 2
        # print(binary)
        n = len(binary)
        complement = 0
        power = 0
        for i in range(n-1,-1,-1):
            if int(binary[i]):
                complement += int(binary[i]) * (2**power)
                power += 1
            else:
                power += 1
        return complement

        return complement

        