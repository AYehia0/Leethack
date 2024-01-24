func finalValueAfterOperations(operations []string) int {
    ans := 0
    m := map[string]int{
        "--X": -1,
        "X--": -1,
        "++X": 1,
        "X++": 1,
    }
    for _, op := range operations {
        ans += m[op]
    }
    return ans
}