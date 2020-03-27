# Given an array, write a function to find any subarray that sums to zero, 
#if one exists.

a = [1,2,-5,1,2,-1]
sum_array = {}
flag=0

for i in range(len(a)):        
    if sum(a[:i+1]) in sum_array:
        print(a[sum(a[:i+1]) : i+1])
        flag=1
        break
    sum_array[sum(a[:i+1])] = i

if flag==0:
    print ([])