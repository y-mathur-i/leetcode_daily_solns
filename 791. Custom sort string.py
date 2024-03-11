class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ord_ = {l:i for i,l in enumerate(order)}
        return "".join(sorted(s, key=lambda x : ord_.get(x, float("inf"))))