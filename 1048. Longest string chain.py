from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        As we are allowed to insert one word anywhere
        For any word we can one by one remove a letter and see if 
        the word exists in the seen bracket
        Sort the words by len in increasing order to guarantee we
        move towards larger len word and all the possible words if there are behind it
        Once i find a word formed by omiiting a char
        i set current len to max(cur_len, word_found_len + 1)
        the len in above line represents the length of sequence that ends on that word
        """

        dp = {word: 1 for word in words}
        words.sort(key=lambda x : len(x))
        res = 0
        for word in words:
            for i in range(len(word)):
                poss = word[:i] + word[i+1:]
                if poss in dp:
                    dp[word] = max(dp[word], dp[poss]+1)
            res = max(dp[word], res)
        return res
