class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        out = [0] * length

        for i in range(length):
            for j in range(i, length):
                if temperatures[j] > temperatures[i]:
                    out[i] = j - i
                    break
        return out