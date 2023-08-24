class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # how many of these can i fit in a line with minumum one space in between ?
        # at each point need to check if i can add this word in the line 
        # with or without space ? .i.e number of words with len plus number -1 space 
        # if only one word just add remaning as space
        # if multiple join them with 
        res,curr,ln= [],[],0
        for word in words:
            if len(curr) + ln+len(word) > maxWidth:
                for i in range(maxWidth-ln):
                    curr[i%(len(curr)-1 or 1)] += ' '
                res.append(''.join(curr))
                curr,ln = [],0
            curr.append(word)
            ln += len(word)
        res.append(' '.join(curr).ljust(maxWidth))
        return res
