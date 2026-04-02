class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let sumAll = 1;
	    let solution = [];
	    for (let i = 0; i < nums.length; i++) {
		    sumAll *= nums[i];
	    }
	    for (let i = 0; i < nums.length; i++) {
		    if (nums[i] !== 0) {
                const n = sumAll / (nums[i] === 0 ? 1 : nums[i]);
		        solution.push(n);
            } else {
                let nWithoutZero = 1;
                for (let j = 0; j < nums.length; j++) {
                    if (i !== j) {
                        nWithoutZero *= nums[j]
                    }
                }
                solution.push(nWithoutZero)
            }
	    }
	    return solution
    }
}
