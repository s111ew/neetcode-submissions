class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        out = []
        for i in range(0, len(words)):
            for j in range(0, len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    out.append(words[i])
                    break
        return out