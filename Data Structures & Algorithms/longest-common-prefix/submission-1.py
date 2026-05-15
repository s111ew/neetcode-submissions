class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while i < len(strs[0]):
            for j in range(1, len(strs)):
                if i > len(strs[j]) - 1 or strs[j][i] != strs[0][i]:
                    return strs[0][0:i]
            i+=1
        return strs[0]
