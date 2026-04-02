func topKFrequent(nums []int, k int) []int {
    freq := make(map[int]int, len(nums))
    
    for _, n := range nums {
        freq[n]++
    }

    buckets := make([][]int, len(nums) + 1)

    for n, f := range freq {
        buckets[f] = append(buckets[f], n)
    }

    var res []int

    for i := len(buckets) - 1; i > 0; i-- {
        for _, v := range buckets[i] {
            res = append(res, v)
            if len(res) >= k {
                return res
            }
        }
    }

    return res
}
