class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dict_set = set(dictionary)
        sentence = list(sentence.split(" "))
        n = len(sentence)
        
        for i in range(n):
            word = sentence[i]
            m = len(word)
            for j in range(m):
                if word[:j+1] in dict_set:
                    sentence[i] = word[:j+1]
                    found = True
                    break
            
        return " ".join(sentence)
            


        