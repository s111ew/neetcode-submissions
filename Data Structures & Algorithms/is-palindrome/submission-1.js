class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
       	const str = s.toLowerCase().split('');
	
	    function isValidChar(char) {
		    if ((char >= 'a' && char <= 'z') || (char >= '0' && char <= '9')) {
			    return true
		    } else {
			    return false
		    }
	    }
	
	    let i = 0;
	    let j = str.length - 1;

	    while (i < j) {
		    while (!isValidChar(str[i]) && i < j) {
			    i++
		    }
		    while (!isValidChar(str[j]) && i < j) {
			    j--
		    }
		    if (str[i] !== str[j]) {
			    return false
		    }
            i++;
            j--;
	    }
	    return true
    }
}
