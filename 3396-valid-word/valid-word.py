class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False
        
        if not word.isalnum():
            return False
        
        vowels = set("aeiouAEIOU")

        if not any(ch in vowels for ch in word):
            return False
        
        if not any(ch.isalpha() and ch not in vowels for ch in word):
            return False
        
        return True