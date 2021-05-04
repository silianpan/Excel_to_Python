set1={1,2,3,4,5,6} #集合1。
set2={4,5,6,7,8,9} #集合2。
set3=set1.difference(set2);print(set3) #集合1减去集合2，结果可以存储在新集合3。
set3=set2.difference(set1);print(set3) #集合2减去集合1，结果可以存储在新集合3。
set3=set1-set2;print(set3) #集合1减去集合2，结果可以存储在新集合3。
set3=set2-set1;print(set3) #集合2减去集合1，结果可以存储在新集合3。
set1.difference_update(set2);print(set1) #集合1减去集合2，差集结果存储在集合1中。
set2.difference_update(set1);print(set2) #集合2减去集合1，差集结果存储在集合2中。
