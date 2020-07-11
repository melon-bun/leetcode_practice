# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 00:16:38 2020

@author: Y410P
"""
import math
class Solution:
    def fib(self, n: int) -> int:
        if n in [0,1]:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
        pass

a = Solution()
print(a.fib(30))


def fac(n):
    if n == 0:
        return 1
    opt = fac(n-1)*n
    return opt
print(fac(4))