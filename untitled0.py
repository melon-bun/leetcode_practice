# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 00:16:38 2020

@author: Y410P
"""
import math
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bot_list = [numBottles]
        res_bot = 0
        while numBottles>=numExchange:
            exchange_bot = numBottles//numExchange
            bot_list.append(exchange_bot)
            res_bot = numBottles%numExchange
            numBottles = exchange_bot + res_bot
        return sum(bot_list)
            
        

        
        
        pass
a = Solution()
print(a.numWaterBottles(15,4))


def fac(n):
    if n == 0:
        return 1
    opt = fac(n-1)*n
    return opt
print(fac(4))