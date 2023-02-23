import (
    "sort"
    "strings"
)

func sortString(w string) string {
    s := strings.Split(w, "")
    sort.Strings(s)
    return strings.Join(s, "")
}

func groupAnagrams(strs []string) [][]string {
    groupAnagrams := make([][]string, 0)
    h := make(map[string][]string)
    
	for _, str := range strs {
		s := sortString(str)
		h[s] = append(h[s], str)
	}
	for _, v := range h {
		groupAnagrams = append(groupAnagrams, v)
	}
	return groupAnagrams

}