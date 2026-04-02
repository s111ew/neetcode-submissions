class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = {};
	    for (let i = 0; i < strs.length; i++) {
		    let s = toChars(strs[i]);
		    if (map[s] === undefined) {
			    map[s] = [strs[i]];
		    } else {
			    map[s].push(strs[i]);
		    }
	    }

	    function toChars(str) {
		    const arr = new Array(26).fill(0);
		    for (let i = 0; i < str.length; i++) {
			    arr[str[i].charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
		    }
		    return arr.join(',');
	    }
	    return Object.values(map);
    }
}
