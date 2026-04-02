class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let seen = {};
	    for (let i = 0; i < nums.length; i++) {
		    const num = nums[i];
		    const remainder = target - nums[i];
		    if (seen[remainder] !== undefined) {
			    return [seen[remainder], i];
		    } else {
			    seen[num] = i;
		    }
	    }
    }
}
