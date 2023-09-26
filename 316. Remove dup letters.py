class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        idxs = {e: i for i, e in enumerate(s)}
        done = set()
        for i, l in enumerate(s):
            if l not in done:
                while stk and stk[-1] > l and idxs[stk[-1]] > i:
                    done.remove(stk.pop())
                stk.append(l)
                done.add(l)
        return "".join(stk)
