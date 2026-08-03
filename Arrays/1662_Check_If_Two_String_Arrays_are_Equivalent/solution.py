class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_new1, word_new2 = '', ''

        for word in word1:
            word_new1 += word

        for word in word2:
            word_new2 += word

        return word_new1 == word_new2
