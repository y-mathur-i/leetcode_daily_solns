class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0]*26
        def convert_to_number(l):
            return ord(l) - ord('a')
        for l in s:
            freq[convert_to_number(l)] += 1

        with_freq_one = set()
        for i, e in enumerate(freq):
            if e == 1:
                ele = chr(ord('a') + i)
                with_freq_one.add(ele)
        for idx, ele in enumerate(s):
            if ele in with_freq_one:
                return idx
        return -1
