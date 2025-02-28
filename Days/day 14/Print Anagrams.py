#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        dic={}
        for i in arr:
            w=''.join(sorted(i))
            if w in dic:
                dic[w].append(i)
            else:
                dic[w]=[i]
        return list(dic.values())
