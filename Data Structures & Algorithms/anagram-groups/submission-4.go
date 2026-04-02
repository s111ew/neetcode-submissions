func groupAnagrams(strs []string) [][]string {
    groups :=  make(map[[26]int][]string, len(strs))

    for _, str := range strs {
        freqArr := createFreqArray(str)
        groups[freqArr] = append(groups[freqArr], str)
    }

    var output [][]string

    for _, strArr := range groups {
        output = append(output, strArr)
    }

    return output
}

func createFreqArray (str string) [26]int {
    var freq [26]int

    for _, n := range str {
        freq[n - 'a']++
    }

    return freq
}