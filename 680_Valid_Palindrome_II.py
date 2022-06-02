'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 
Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True # return True if the string is already a palindrome
        left = 0
        right=len(s)-1

        while(left<=right):
            if s[left] != s[right]: # keep checking if the characters are same
                if s[left: right] == s[left: right][::-1] or s[left+1: right+1][::-1] == s[left+1: right+1]:  # if not same then the smaller string excluding 1 charcter from either left or right should be a palindrome
                    return True
                else:
                    return False
            else:
                left += 1 # keep moving right
                right -= 1 # keep moving left