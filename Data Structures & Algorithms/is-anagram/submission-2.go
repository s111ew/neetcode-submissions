func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    chars := make(map[rune]int)

    for _, char_s := range s {
        chars[char_s]++
    }

    for _, char_t := range t {
        n, ok := chars[char_t]
        if !ok || n == 0 {
            return false 
        }

        chars[char_t]--
    }

    for _, val := range chars {
        if val != 0 {
            return false
        }
    }

    return true
}
