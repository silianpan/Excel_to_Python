set1={1,2,3,4,5,6} #集合1。
set2={4,5,6,7,8,9} #集合2。
set3=set1.symmetric_difference(set2);print(set3)#去掉集合1与集合2相同元素，结果存储在新集合3。
set3=set2.symmetric_difference(set1);print(set3)#去掉集合2与集合1相同元素，结果存储在新集合3。
set3=set1^set2;print(set3)#去掉集合1与集合2相同元素，结果存储在新集合3。
set3=set2^set1;print(set3)#去掉集合2与集合1相同元素，结果存储在新集合3。
set1.symmetric_difference_update(set2);print(set1)#去掉集合1与集合2相同元素，结果可以存储在集合1。
set2.symmetric_difference_update(set1);print(set2)#去掉集合2与集合1相同元素，结果可以存储在集合2。
