'''n=int(input())
while(True):
    if str(n+1)[::-1]==str(n+1):
        print(n+1)
        break
    n=n+1
imp[ort sys
def Next_smallest_Palindrome(num):
    for i in range(num+1,sys.maximize):  #101
        if str(i)==str(i)[::1]:#101=101 1==1 0==0
            return i
print(Next_smallest_Palindrome(99))
print(Next_smallest_Palindrome(1221))'''
#hospital catogery
'''n=list(map(str,input().split()))
dic={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
if n.count("P")>n.count("O") and n.count("P")>n.count("E"):
    print("Pediatrics")
elif n.count("O")>n.count("P")and n.count("O")>n.count("E"):
    print("Orthopedics")
else:
    print("ENT")'''
#common character
'''st1="I like Python"
st2="Java is avery popular language"
st1=st1.replace(" ","")
st2=st2.replace(" ","")

l=[]
for i in st1:
    for j in st2:
        if ord(i)==ord(j):
            l.append(i)
l=set(l)
if l==[]:
    print(-1)
else:
    for i in list(l):
        print(i,end="")'''
#class
'''
class Example:
    def_init_(self,num):
        self.num=num

    def set_num(self,num):
        return self.num

obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())'''

'''class Customer:
    def _init_(self):
        cust_id=100
c1=Customer()
print(c1.cust_id)
'''
'''class Customer:
    def _init_(self,id):
        self.id = 100
c1=Customer(200)
print(c1.id)
class Customer:
    def _init_(self,id):
        self.id = id
c1=Customer(200)
print(c1.id)'''

'''class Book:
    def __init__(self):
        self.title=Npne
my_fav=Book()
my_fav.title="Head First Programing"
your_fav=Book()
your_fav.title="Learn Python the hard way"

my_fav.title="Learning Python"

print("My favourite is",my_fav.title)
print("Your's is",your_fav.title)'''
"""class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
        
s1=Shoe(1000,"Canvas")
print(s1)
print(s1.price,s1.material)
print("the unique id of the object",id(s1))"""

'''class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material

   def __str__(self):#way of creating new default string in place of previous default
        return "Shoe with price: " + str(self.price) + "and material:" +self.material
s1=Shoe(1000,"Canvas")
print(s1)'''

'''class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")

    def purchase(self):
        self.display()
        print("Calculating price")

#Mobile().purchase()
m1=Mobile()#100
print(m1)
m2=Mobile()#200
print(m2)
m1=m2#200
print(m1)#200
print(m2)#200'''
'''class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
        self.total_price = None
    def purchase(self):
        if self.brand == "Apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price - self.price*(discount/100)
        print("total_price of",self.brand,"mobile is",self.total_price)
    def amount_returned(self):
        return(self.price-self.total_price)
        
mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amount_returned())
print(mob2.amount_returned())'''
'''class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance#__before wallet we can change wallet from public to private
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance+=amount
    def show_balance(self):
        print("The balance is ",self.wallet_balance)
    def get_wallet_balance(self):#way to call  private value
        return self.__wallet_balance
print(c1.__wallet_balance())
        
c1=Customer(100, "Gopal",24,1000)
c1.update_balance(500)
c1.show_balance()'''
'''class Dam:
    def _init_(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length


dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam Length",dam1.get_length())'''
'''class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(False, True)
print(rate)'''
class Table:
    def __init__(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)









        

           
