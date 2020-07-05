# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 00:16:38 2020

@author: Y410P
"""
import math
class Solution:
    def canMakeArithmeticProgression(self, arr: list) -> bool:
        sorted_arr = sorted(arr)
        delta = sorted_arr[1]-sorted_arr[0]
        for i in range(len(sorted_arr)-1):
            print(arr[i])
            if sorted_arr[i+1]-sorted_arr[i]!=delta:
                return False
        return True
            
            
        
        
        pass
    
        
a = Solution()
print(a.canMakeArithmeticProgression([3,5,1]))