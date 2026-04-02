func twoSum(nums []int, target int) []int {
    pairs := make(map[int]int)

    for i, n := range nums {
        idx, ok := pairs[target - n]
        if ok {
            return []int{idx, i}
        }

        pairs[n] = i
    }

    return nil
}
