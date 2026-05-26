class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Step 1: Create a hash set of all characters present in the word
        char_set = set(word)
        special_count = 0
        
        # Step 2: Track lowercase characters we have already evaluated 
        # to ensure we only count each unique special letter once
        counted_lowercase = set()
        
        # Step 3: Iterate through the string
        for char in word:
            # Check if it's a lowercase letter and we haven't counted it yet
            if char.islower() and char not in counted_lowercase:
                # Check if its uppercase version exists in our hash set
                if char.upper() in char_set:
                    special_count += 1
                    counted_lowercase.add(char) # Mark as counted
                    
        return special_count