class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let currentMax = 0;
	    let left = 0;
	    let right = heights.length - 1;
	    while (left < right) {
		    currentMax = Math.max(currentMax, ((right - left) * Math.min(heights[left], heights[right])));
		    if (heights[left] >= heights[right]) {
			    right--;
		    } else {
			    left++;
		    }
	    }
	    return currentMax;	
    }
}
