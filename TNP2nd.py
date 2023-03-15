#LIST
'''list1=[]
print(list1,type(list1))
list2=[10,20,30,40]
print(list2,type(list2))
list3=[10,20.2,30+5j,True,"python"]
print(list3,type(list3))
list5=list([101,201,301])
print(list5,type(list5))
list5.append(401)
print(list5,type(list5))
list5.extend([501,601,701])
print(list5,type(list5))
list5.insert(4,350)#index,value
print(list5,type(list5))
list5.remove(701)
print(list5,type(list5))
list5.pop(0)
print(list5,type(list5))
del list5[1]
print(list5,type(list5))
def function(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return[l_count,d_count]
print(function("Infosys 123"))
def pairs(lst,n):
    c=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j] == n:
                c=c+1
    return c
lst=list(map(int,input().split()))
n=int(input())
print(pairs(lst,n))
def function1(str1):
    if len(str1)<2:
        return -1
    else:
        st=str1[0:2]+str1[-2:]
        return st
print(function1("w3resource"))
print(function1("w3"))
print(function1("A''))

st=input()
if 'ing' in st:
    print(st+"ly")
elif len(st)<3:
    print(st)
else:
    print(st+"ing")'''
'''def check_double(n):
    c=0
    double=2*n
    print(double)
    for i in str(n):
        if i in str(double) and len(str(double))==len(str(n)):
              c+=1
      
    if(c==len(str(n))):
       return True
    else:
        return False
n=int(input())
print(check_double(n))
def more_average(marks):
    l=[]
    avg=sum(marks)/len(marks)
    for i in marks:
        if i>=avg:
            l.append(i)
    per=(len(l)/len(marks))*100
    return per

def count_marks(marks):
    l=[]
    for i in range(25):
        l.append(marks.count(i))
    return l
def sort_marks(marks):
    l=list(marks)
    l.sort()
    return l
marks=tuple(map(int,input().split()))
print(more_average(marks))
print(count_marks(marks))
print(sort_marks(marks))

def translate(dic,lst):
    for i in lst:
        print(dic[i],end=" ")

dic={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
lst=list(map(str,input().split()))
translate(dic,lst)'''
n1=int(input())
n2=int(input())
l=list(map(int,input().split()))
lst=[]
c=0
for i in range(len(l)+1):
    for j in range(i):
        lst.append(l[j:i])
print(lst)
for i in lst:
    if sum(i)%2!=0:
        c+=1
print(c)


    
    

