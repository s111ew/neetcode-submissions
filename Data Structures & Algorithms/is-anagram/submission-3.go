func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    var chars [26]int

    for i := 0; i < len(s); i++ {
        chars[s[i] - 'a']++
        chars[t[i] - 'a']--
    }

    for _, v := range chars {
        if v != 0 {
            return false
        }
    }

    return true
}
