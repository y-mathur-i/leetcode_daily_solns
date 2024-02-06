class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = defaultdict(list)
        for word in strs:
            srtd_word = "".join(sorted(list(word)))
            di[srtd_word].append(word)
        return list(di.values())
