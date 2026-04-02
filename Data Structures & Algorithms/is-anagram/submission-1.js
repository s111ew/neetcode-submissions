class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        const seen = {};
	    for (const char of s) {
		if (seen[char] === undefined) {
			seen[char] = 1;
		} else {
			seen[char] += 1;
		}
	    }
	    for (const char of t) {
		if (seen[char] === undefined) {
			return false;
		} else {
			if (seen[char] === 0) {
				return false;
			}
			seen[char] -= 1;
		}
	}
	for (const key in seen) {
		if (seen[key] !== 0) {
			return false;
		}
	}
	return true
    }
}
