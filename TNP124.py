"""name="shashi"
print("name",name,type(name))
n=int(input())
if(n%3==0 and n%5==0):
    print("multiple of both 3 and 5")
elif(n%3==0):
    print("multiple of 3")
elif(n%5==0):
    print("multiple of 5")
else:
    print("invalid input")"""
#range(start,end,step)
#for i in range(100,0,-2):
       #print(i,end=' ')
#for i in range(99,0,-2):
  #  print(i,end=' ')
# 100 98 ...2
#for i in range(100,1,-2):
    #print(i,end=' ')
#break
'''for i in range(1,100):
    if (i == 50):
        break
    else:
        print(i)
for i in range(1,100):
    if (i == 50):
        continue
    print(i,end= ' ')'''
#functions
'''def funcionl():
    print("its a function")
functional()
def functionl2(num1 ,num2):
    print("num1=",num1,"num2=",num2)
    #prin()_str_
funcion2(10,20)
def function3(num1,num2):
    num3=num1+num2
    return num3
print("value returned",function3(100,200))
def function4(num1,num2):
    num4=float(num1)+num2
    return num4
print("value returned",function4('10',20.2))
def function5(num1,num2):
    num5=num1+num2
    return num5
print("value returned",function5('10','20.2'))
#categories of functions
def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,20,30,40)
function1(10,"200",20,40)
#keyword arguments
def function2(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=10,num1=20,num2=30,num3=40)
#3 default argument
def function3(name,rollno,branch="CSE",collegename="GIET "):
    print(name,rollno,branch,collegename)
function3("aditya",11)
function3("shashi",12)
function3("aditi",13,"CSt")
function3("ravi",114,"ECE")
def functional4(*var):#tuple
    for i in var:
        print(i,end=' ')
functional4(10,20)
print()
functional4(10,20,30,40)
print()
functional4(10,20,30,40,50,60)
print()
def add(*var):#tuple
    sum1=0
    for i in var:#10,20
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50,60))
#LIST
num1=int(input())
num2=int(input())
num3=int(input())
if num1==7:
    print(num2*num3)
elif num2==7:
    print(num3)
elif num3==7:
    print(-1)
else:
    print(num1*num2*num3)
    
def currencycal(AmountINR,curr):
     if curr=="Euro":
         print(AmountINR*0.01417)
     elif curr=="British Pound":
         print(AmountINR*0.0100)
     elif curr=="Australian Dollar":
         print(AmountINR*0.02140)
     elif curr=="Canadian Dollar":
         print(AmountINR*0.02027)
     else:
         print(-1)
currencycal(300,"Euro")
adult=int(input())
child=int(input())
amount= 37550*adult+((1/3)*37550*child)
TotalTax= amount+((7/100)*amount)
total=TotalTax-((10/100)*TotalTax)
print(total)'''
r1=int(input())
r5=int(input())
money=int(input())
print("number of 5  rupee",money//5)
print("number of 1 rupee",money%5)
if money%5>r1:
    print(-1)   


    
    





    
    
    





    
    
    
