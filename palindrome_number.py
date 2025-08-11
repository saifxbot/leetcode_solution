class Solution(object):
    def isPalindrome(self, x): # Check if an integer is a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0        # Initialize the reversed half of the number
        while x > reversed_half: # Reverse the last half of the number
            reversed_half = reversed_half * 10 + x % 10 # Build the reversed half
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10  # Check if the original number is equal to the reversed half or the reversed half without the last digit
