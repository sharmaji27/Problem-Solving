# Given 2 sorted arrays, A and B, where A is long enough to hold the contents of
# A and B, write a function to copy the contents of B into A without using any buffer or
# additional memory.

a = [1,2,5,0,0,0]
b = [2,18,20]

for i in range(len(a)):
    if a[i]!= 0:
        continue
    p=i-1
    break
    
up = len(a)-1
down = len(b)-1


while down != -1:
    if a[p] > b[down]:
        a[up] = a[p]
        up-=1
        p-=1
        
    else:
        a[up] = b[down]
        up-=1
        down-=1