class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = -1

        for i in range(len(letters)):
            if (ans == -1 and ord(letters[i]) > ord(target)) or (ord(letters[i]) > ord(target) and ord(letters[i]) < ord(letters[ans])):
                ans = i
        
        return letters[ans] if ans != -1 else letters[0]