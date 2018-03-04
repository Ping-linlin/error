# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     004-defaultdict
   Description :    dict.setdefault.method 只能对可变对象进行原地运算.
                    如下例, 最好使用defaultdict
   Author :       pinglin
   date：          18-3-4
-------------------------------------------------
"""
from collections import defaultdict
ss = "fweowingejrwoirjejwwo"
my_dict = defaultdict(int)

for item in ss:
    my_dict[item] += 1

print(my_dict)

# my_dict.setdefault(key, []).append(value)