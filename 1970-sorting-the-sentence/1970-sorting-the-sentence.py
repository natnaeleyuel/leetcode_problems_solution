class Solution:
    def sortSentence(self, s: str) -> str:
        listWord = s.split()
        resultW = ['']*len(listWord)
        for word in listWord:
            l = int(word[len(word) - 1]) - 1
            resultW[l] = word[:len(word)-1]
        return ' '.join(resultW)    