#In python there is only pass by reference
"""def s(l):
    l[0]=20
lx=[2,3,4,5]
s(lx)
print(lx)"""
#fact
"""n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print(f)  """  
#fact rec
"""def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
x=int(input())
s=fact(x)
print(s)"""
#fib rec
"""def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
x=fib(7)
print(x)"""
#sugarcane codechef
"""def profits(n):
    n=n*50
    n=n-70/100*n
    return n
t= int(input())
for _ in range(t):
    x=int(input())
    y=profits(x)
    print(y)"""
#sugarcane rec
'''
t=int(input())
def prof(n):
    x=int(n-70/100*n)
    return x
def test(m):
    if m>0:
        n=int(input())
        print(prof(n))
    else:
        return
    test(t-1)
test(t)
'''
#movie
'''
for i in range(int(input())):
    x=int(input())
    y=int(input())
    print(y//2+(x-y))
'''

'''def mov(n,m):
    print(n-m+(m//2))
a,b=map(int,input().split())
mov(a,b)'''
#lucky four
"""
for i in range()"""
#3
"""def add3(n):
    ans=3*10000+n*10+3
    print(ans)
for _ in range(int(input())):
    add3(int(input()))"""
#
"""def add3(n):
    x=n
    c=0
    while(n):
        c+=1
        n=n//10
    ans=3*(10**(c+1))+x*10+3
    print(ans)
for _ in range(int(input())):
    add3(int(input()))"""