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
#pizza
'''class customer:
   # def __init__(self):
      
      def validate_quantity(self,number):
          self.number=number
          if 0<self.number<=5:
              return True
          else:
              return False


class pizzasevices:
    #customer.validate_quantity(self.number)
    counter=100
    def __init__(self):
        self.quantity=None
        self.pizzasize=None
        self.topping=None
     # self.cost=None
    def pizza_attr(self,quantitypizzasize,topping,):
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
                print("price of pizza is:",(185*self.quantity))
            else:
                print("price of pizza is:",(250*self.quantity))
        else:
            if pizzasize=="small":
                print("price of pizza is:",(150*self.quantity))
            else:
                print("price of pizza is:",(200*self.quantity))
            
            
    
        


class doordelivery:
    pizzasevices.pizzacost(cost)

    def validate_distance_in_km(self,distance):
        if 1<=self.distance<=5:
            self.pizzacost=self.pizzacost+5
        else:
            self.pizzacost=self+5+7'''
#pizza delivery
class Customer:
    def validate_quantity(self, quantity):
        if quantity >= 1 and quantity <= 5:
            return True
        else:
            return False

class PizzaService:
    counter = 100
    
    def _init_(self, pizza_type, quantity, additional_topping):
        self.pizza_type = pizza_type
        self.quantity = quantity
        self.additional_topping = additional_topping
        self.pizza_cost = -1
        
    def validate_pizza_type(self):
        if self.pizza_type.lower() == "small" or self.pizza_type.lower() == "medium":
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer().validate_quantity(self.quantity):
            pizza_cost_table = {"small": 150, "medium": 200}
            additional_topping_cost_table = {"small": 35, "medium": 50}
            
            pizza_cost = pizza_cost_table[self.pizza_type.lower()] * self.quantity
            if self.additional_topping:
                pizza_cost += additional_topping_cost_table[self.pizza_type.lower()] * self.quantity
                
            self.pizza_cost = pizza_cost
            self.service_id = self.pizza_type[0].upper() + str(PizzaService.counter + 1)
            PizzaService.counter += 1
            
        else:
            self.pizza_cost = -1
    
class DoorDelivery(PizzaService):
    def _init_(self, pizza_type, quantity, additional_topping, distance_in_kms):
        super()._init_(pizza_type, quantity, additional_topping)
        self.distance_in_kms = distance_in_kms
        
    def validate_distance_in_kms(self):
        if self.distance_in_kms >= 1 and self.distance_in_kms <= 10:
            return True
        else:
            return False
        
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms() and super().calculate_pizza_cost() != -1:
            delivery_charge_table = {1: 5, 6: 7}
            
            if self.distance_in_kms <= 5:
                self.pizza_cost += delivery_charge_table[1] * self.quantity
            else:
                self.pizza_cost += delivery_charge_table[1] * self.quantity
                self.pizza_cost += delivery_charge_table[6] * (self.distance_in_kms - 5) * self.quantity
                
        else:
            self.pizza_cost = -1

# Testing
pizza_service = PizzaService("Small", 3, True)
pizza_service.calculate_pizza_cost()
print("Service ID:", pizza_service.service_id)
print("Pizza cost:", pizza_service.pizza_cost)

door_delivery = DoorDelivery("Medium", 2, False, 8)
door_delivery.calculate_pizza_cost()
print("Service ID:", door_delivery.service_id)
print("Pizza cost:", door_delivery.pizza_cost)




    

        

    
