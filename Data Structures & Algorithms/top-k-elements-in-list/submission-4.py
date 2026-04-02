class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if freq.get(num) is None:
                freq[num] = 1
            else:
                freq[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in freq.items():
            buckets[value].append(key)

        out = []
        for bucket in reversed(buckets):
            if bucket != []:
                for n in bucket:
                    out.append(n)
                    if len(out) == k:
                        return out