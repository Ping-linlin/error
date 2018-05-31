# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     list_remove_error
   Description :
   Author :       pinglin
   date：          18-1-7
-------------------------------------------------
   Change Activity:
                   18-1-7:
-------------------------------------------------
"""
__author__ = 'pinglin'

d = [1,2,3,4,5]
for i in d:
    d.remove(i)
print(d) # [2, 4]
# 第一次循环，删除d[0] 此时d = [2,3,4,5]
# 然后i = 1 删除d[1] 对应此时列表中的3




