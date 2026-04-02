class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const solution = [];
	    const sorted = nums.sort((a, b) => a - b);
	    for (let i = 0; i < sorted.length; i++) {
		    if ((i === 0 || sorted[i] !== sorted[i - 1]) && sorted[i] < 1) {
			    let l = i + 1;
			    let r = sorted.length - 1;
	            while (l < r) {
		            const sum = sorted[i] + sorted[l] + sorted[r];
		            if (sum === 0) {
			            solution.push([sorted[i], sorted[l], sorted[r]]);
                        while (l < r && nums[l] === nums[l + 1]) l++;
                        while (l < r && nums[r] === nums[r - 1]) r--;
                        l++;
                        r--;
		            } else if (sum < 0) {
			            l++;
		            } else if (sum > 0) {
			            r--;
		            }
	            }	
            }
	    }
	    return solution;
    }
}
