class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = {};
	    for (let i = 0; i < nums.length; i++) {
		    if (freq[nums[i]] === undefined) {
			    freq[nums[i]] = 1;
		    } else {
			    freq[nums[i]] += 1;
		    }
	    }

	    const sorted = Object.entries(freq)
		    .sort((a, b) => b[1] - a[1])
		    .slice(0, k)
		    .map(([num]) => Number(num));

	    return sorted
    }
}
