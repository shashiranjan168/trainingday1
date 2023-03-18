'''class vechiles:
    def __init__(self):
        self.__vechile_id=None
        self.__cost=None
        self.__vechile_type=None
    def set_attr(self,vechile_id,vechile_type,cost):
        self.__vechile_id=vechile_id
        self.__vechile_type=vechile_type
        self.__cost=cost

    def get_cal(self):
        if self.__vechile_type != "Two vechiler" and self.__vechile_type != "Four vechiler":
            print("Invalid Message")
        elif self.__vechile_type == "Two vechiler":
            self.__amt=(2/100)*self.__cost
        else:
            self.__amt=(6/100)*self.__cost
        return self.__amt

v1=vechiles()
v1.set_attr(101,"Two vechiler",10000)
print(v1.get_cal())
v2=vechiles()
v2.set_attr(102,"Four vechiler",50000)
print(v2.get_cal())'''
#university addmission:
'''class student:
    def __init__(self):
        self.student_id=None
        self.age=None
        self.marks=None
      #  self.fees=None
    def set_studentattr(self,student_id,age,marks):
        self.student_id=student_id
        self.age=age
        self.marks=marks
       # self.fees=fees
    def validate_marks(self):
        if 0<=self.marks<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.age>20:
            return True
        else:
            return False

    def  check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.marks>65:
                print("course id : 1001, 1002")
                print("course fee for course id 1001 : 25575 , course fee for course id 1002 : 15500" )
                return True
            else:
                return False
    def discount(self):
        if self.check_qualification() and self.marks>85:
            pay=(25575-(25575 * (1/4)))
            return (pay)
        else:
            return False
s1=student()
s1.set_studentattr(300,22,90)
print(s1.check_qualification())
print(s1.discount())
print("course id : ",1001 , "course fee:" ,s1.discount())'''

class customer:
   # def __init__(self):
      
      def validate_quantity(self,number):
          self.number=None
          if 0<self.number<=5:
              return True
          else:
              return False


class pizzasevices:
    customer.validate_quantity(self,number)
    counter=100
    def __init__(self):
        self.pizzasize=None
        self.topping=None
     #   self.cost=None
    def pizza_attr(self,pizzasize,topping,):
        self.pizzasize=pizzasize
     #   self.cost=cost
        self.topping=topping
    def add_topping(self):
        toppingBool == True
        if toppingBool == True:
            return True
        else:
             return False
    def pizzasize(self):
        if pizzasize=="small" or pizzasize=="medium":
            return True
        else:
            return False
    def pizzacost(self):
        if self.pizzasize() and self.add_topping():
            if pizzasize=="small":
                print("price of pizza is:",(185*self.number))
            else:
                print("price of pizza is:",(250*self.number))
        else:
            if pizzasize=="small":
                print("price of pizza is:",(150*self.number))
            else:
                print("price of pizza is:",(200*self.number))
            
            
    
        


class doordelivery:
    pizzasevices.pizzacost(cost)

    def validate_distance_in_km(self,distance):
        if 1<=self.distance<=5:
            self.pizzacost=self.pizzacost+5
        else:
            self.pizzacost=self+5+7
        

    

        

    
