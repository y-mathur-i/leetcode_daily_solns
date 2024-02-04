class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        req = Counter(t)
        i = j = 0
        ln = float("inf")
        needed = len(t)
        l = 0
        for r, e in enumerate(s):
            if e in req: # it is a required key
                req[e] -= 1
                needed -= 1 if req[e] >= 0 else 0
            while not needed and req.get(s[l], -1) <= 0:
                if s[l] in req:
                    req[s[l]] += 1
                    needed += 1 if req[s[l]] > 0 else 0
                if ln > r-l:
                    i, j = l, r
                    ln = r-l
                l += 1
        return s[i:j+1] if ln != float("inf") else ""
