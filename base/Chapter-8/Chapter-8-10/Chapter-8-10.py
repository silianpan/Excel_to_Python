set1={1,2,3,4,5,6}#集合1。
set2={4,5,6,7,8,9}#集合2。
set3=set1.intersection(set2);print(set3)#集合1与集合2交集，结果可以存储在新集合3。
set3=set2.intersection(set1);print(set3)#集合2与集合1交集，结果可以存储在新集合3。
set3=set1&set2;print(set3)#集合1与集合2交集，结果可以存储在新集合3。
set3=set2&set1;print(set3)#集合2与集合1交集，结果可以存储在新集合3。
set1.intersection_update(set2);print(set1)#集合1与集合2交集，交集结果存储在集合1。
set2.intersection_update(set1);print(set2)#集合2与集合1交集，交集结果存储在集合2。