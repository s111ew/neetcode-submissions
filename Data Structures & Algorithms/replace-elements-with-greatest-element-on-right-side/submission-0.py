class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        currMax = -1

        while i >= 0:
            tmp = arr [i]
            arr[i] = currMax
            currMax = max(currMax, tmp)
            i -= 1

        return arr