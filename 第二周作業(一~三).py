# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:24:06 2022

@author: AMY
"""
"""作業一
1
22
333
4444
55555
"""
for a in range(1,6): #[1,2,3,4,5]
    for b in range(a): # [0,1,2,3,4] a=>5次
        print(a,end='') 
    print()

print("作業一程式執行完畢")


"""
作業二
55555
4444
333
22
1
"""
for a in range(5,0,-1): #[5,4,3,2,1]
    for b in range(a): # [0,1,2,3,4] a=>5次
        print(a,end='') 
    print()
print("作業二程式執行完畢")

"""
作業三
999999999
7777777
55555
333
1
"""
for a in range(9,0,-2): #[9,7,5,3,1]
    for b in range(a): # [0,1,2,3,4,5,6,7,8] a=>9次、7次、5次、3次、1次
        print(a,end='') 
    print()
print("作業三程式執行完畢")


