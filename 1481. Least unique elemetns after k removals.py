class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        keys = sorted(list(k for k in cnt.keys()), key=lambda x : cnt[x])
        for key in keys:
            val = cnt[key]
            if val <= k:
                k -= val
                del cnt[key]
            else:
                return len(cnt.keys())
        return 0
