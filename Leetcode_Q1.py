'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index,i in enumerate(nums):
            rem = target - i
            arr = nums.copy()
        ##-------We have to use .copy() for copying the original list to a new list.------------## 
        ##--------Otherwise the new list will just be a referrence to the original list.--------##
            arr.remove(i)
            if rem in arr:
                return [index,nums.index(rem,index+1)] 
        ##--------Key concept: You can specify the starting point of the .index() method.-------------------------##
        ##--------Here I have specified that it should start looking for the element from index+1 position.-------##
            else:
                continue