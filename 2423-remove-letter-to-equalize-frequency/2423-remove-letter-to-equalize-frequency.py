class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        word_freq = defaultdict(int)
        count_freq = defaultdict(int)

        for w in word:
            if w in word_freq:
                count_freq[word_freq[w]] -= 1
                if count_freq[word_freq[w]] == 0:
                    del count_freq[word_freq[w]]
            
            word_freq[w] += 1
            count_freq[word_freq[w]] += 1

        if len(count_freq) == 1 and next(iter(count_freq)) == 1:
            return True
        
        for w in word:
            count_freq[word_freq[w]] -= 1

            if word_freq[w] > 1:
                count_freq[word_freq[w] - 1] += 1

            if count_freq[word_freq[w]] == 0:
                del count_freq[word_freq[w]]

            if len(count_freq) == 1:
                return True

            if word_freq[w] > 1:
                count_freq[word_freq[w] - 1] -= 1

                if count_freq[word_freq[w] - 1] == 0:
                    del count_freq[word_freq[w] - 1]
                    
            count_freq[word_freq[w]] += 1
            
        return False