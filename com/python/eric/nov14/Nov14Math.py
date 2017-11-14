def fib(n):
    if n==0:
     return n
    if n==1:
     return n
    if n>=2:
     return fib(n-1)+fib(n-2)
mm=fib(6)
 #当n=5时,返回fib(4)+fib(3)  fib(3)+fib(2)+
print(mm)

def yuese(n,k):
    index=0
    #针对n个人形成一个列表
    people=list(range(1,n+1))
    while 1:
        if len(people)==2:
            break
        #index是删除的索引值
        index=(index+(k-1))%len(people)
        del people[index]
    print('存活下来的两个幸运的人',people)
mm= yuese(45,3)