class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = {};
        const solution = [];
        for (let i = 0; i < strs.length; i++) {
            const sorted = strs[i].split("").sort().join("");
            if (map[sorted] !== undefined) {
                map[sorted].push(strs[i]);
            } else {
                map[sorted] = [strs[i]];
            }
        }
        for (let key in map) {
            solution.push(map[key]);
        }
        return solution;
    }
}
