class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        if (nums.length === 2) return [0, 1];
	
	    const seen = {};
	    for (let i = 0; i < nums.length; i++) {
		const remainder = target - nums[i];
		if (seen[remainder] !== undefined) {
			return [seen[remainder], i];
		}
		seen[nums[i]] = i;
	}

    }
}
