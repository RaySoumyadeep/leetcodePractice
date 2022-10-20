'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        # Find the shortest word
        shortest_length = min([len(s) for s in strs])
        #Make all the words of same length
        for i, s in enumerate(strs):
            strs[i] = s[:shortest_length]
        
        #Compare the first word with the other words in the list
        while True:
            first_word = strs[0]
            matching_strings = [s for s in strs if s == first_word]
            if len(matching_strings) == len(strs):
                return first_word
            #Reduce each string by one
            for i, s in enumerate(strs):
                strs[i] = s[:-1]
