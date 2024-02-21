#Lists and Tuples
#if spaced integers are given
"""l = input().split()
print(l)"""
#if not spaced
"""l = list(map(int,input()))
print(l)"""
# List methods used
# append() extend() insert() remove() pop() clear() index() count() copy() sort() reverse()
# append to insert at the end
# extend adds a whole list to another list => l=[0,1,2]. l.extend([3,4,5]). now l= [0,1,2,3,4,5]
# insert inserts an element at a particular index =>l = [0,1] l.insert(1,2).value 2 is inserted at index 1. l=[0,2,1]
# but insert increases hell lot of time complexity

#remove() deletes an element based on value => l=[0,1,2] l.remove(1) => l=[0,2]
"""l=[0,1,0,1,1]
l.remove(1)
print(l)"""
#pop() removes last element if no parameter is given else deletes element based on index
"""l=[0,1,0,1,1]
l.pop()#deletes last element
print(l)
l.pop(2)#deletes element at index 2
print(l)"""
#clear() clears all elements in a list and remains empty list

#sort is a method sorted is a function

#Built-in functions
#min() max() sum() all() any() len()
"""l=[12,34,0,45]
print(sum(l)) #prints sum of elemnts in a list
print(max(l)) #prints max element
print(min(l)) #prints min element
print(all(l)) #returns true if none of the element is 0
print(any(l)) #returns true if any element is not 0
print(len(l))"""

#operations on list
#concat l1+l2 repeat l1*3 times membership operators: in, not in
"""l1=[1,2,3,4]
l2=[2,3,4]
print(l1+l2)
print(l1*4)
print(2 in l1)"""
 #slicing 
# ":" is used for slicing

#List comprehension
#list of squares of even numbers of 1to10 numbers
#List Comprehension ==> Output expression(x**2), input sequence(for x in range(1,11)), variable or condition(if x%2==0)
"""a = [x**2 for x in range(1,11) if x%2==0]
print(a)
"""

#PROBLEM PRACTICE ON *LISTS*

#find duplicate
"""n = int(input())#size of array
l = list(map(int,input().split()))[:n]
x=[]
y=[]
for i in range(n):
    if l[i] not in x:
        x.append(l[i])
    else:
        y.append(l[i])
print(y)"""
#AP-2
"""n=int(input())
l = list(map(int,input().split()))[:n]
print(l)
for i in range(n):
    if l[i] in l[i+1:]:
        print(l[i])
        break"""
#AP-3
"""n=int(input())
l = list(map(int,input().split()))[:n]
l.sort()
for i in range(n-1):
    if l[i] == l[i+1]:
        print(l[i])
        break"""
#AP-4
"""n=int(input())
l = list(map(int,input().split()))[:n]
for i in l:
    if l.count(i)>1:
        print(i)
        break"""
#print unique elements
"""n = int(input())#size of array
l = list(map(int,input().split()))[:n]
un=[]
for i in l:
    if l.count(i)==1:
        un.append(i)
print(un)"""
#Tuple
"""t=(2,3,4)
t1=t[::2]
print(t1)"""
#Tuple comprehension cant be done directly instead use list comprehension and then typecast it into tuple
"""t=tuple( i*i for i in range(1,5))
print(t)"""
#chef sum
"""n=int(input())
le=0
lo=1
for i in range(1,n+1):
    if n%i==0:
        print(i)
        if i%2==0:
            le+=1
        else:
            lo+=1
print(le,lo)
if le==lo:
    print("Yes")
else:
    print("No")"""
#p Print if a given number is perfect or not
"""n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        print(i)
        sum+=i
if sum == n:
    print("Yes")
else:
    print("No")"""
#print perfect numbers in a given range
"""n=int(input())
sum=0
for i in range(2,n+1,2):
    for j in range(1,i):
        if i%j == 0:
            sum+=j
    if sum == i:
        print(i)
    sum=0"""