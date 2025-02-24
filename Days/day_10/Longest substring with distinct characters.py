#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        
        # Dictionary to store last positions of characters
        char_index = {}
        max_length = 0
        start = 0
    
        for end, char in enumerate(s):
            # If the character is already in the window, update the start position
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
    
            # Update the last position of the character
            char_index[char] = end
    
            # Calculate the max length
            max_length = max(max_length, end - start + 1)
    
        return max_length
        
