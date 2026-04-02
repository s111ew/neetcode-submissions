class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        if (s.length % 2 !== 0) return false;
	    let dict = {	
		    '}': '{',
		    ']': '[',
		    ')': '(',
		    }
	    let stack = [];
	    for (let i = 0; i < s.length; i++) {
		    if (dict[s[i]] === undefined) {
	            stack.push(s[i]);
            } else {
	            if (dict[s[i]] !== stack[stack.length - 1]) return false;
                stack.pop();
            }
	    }
	    if (stack.length !== 0) return false;
	    return true;
    }
}
