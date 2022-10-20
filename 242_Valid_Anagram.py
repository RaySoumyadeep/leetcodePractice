'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        s_dict, t_dict = {},{}
        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i],0)
            t_dict[t[i]] = 1 + t_dict.get(t[i],0)
        return s_dict == t_dict