class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        keys = sorted((k for k in cnt.keys()), key=lambda x : -cnt[x])
        # print(keys)
        return "".join(list(k*cnt[k] for k in keys))