# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     closure_bind
   Description :
   Author :       pinglin
   date：          18-1-26
-------------------------------------------------
   Change Activity:
                   18-1-26:
-------------------------------------------------
"""
def late_binding():
    return [lambda x: i * x for i in range(4)]


def early_binding():
    return [lambda x, i = i: i * x for i in range(4)]


print([m(3) for m in late_binding()])   # [9, 9, 9, 9]
print([m(3) for m in early_binding()])  # [0, 3, 6, 9]
