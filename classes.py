# class Bank_acc:
#     def __init__(self,accName,accNum,bal)
#         self.accName = accName
#         self.accNum = accNum
#         self.bal = bal
#     def Deposit(self):
#         deposit = 200000
#         self.deposit= deposit+self.acctbal
#         return self.deposit
#     def withdraw(self):
#         withdraw = 150000
#         self.withdraw = self.deposit - withdraw
#         return self.withdraw
#     def availablebalance(self):
#         balance = self.withdraw
#         return balance
    
# Bank_Acc = Bank_acc('Temmy',1999000000, 5000000)
# Bank_Acc2 = Bank_acc('Ayo', 3334826232, 300000)
# print(f"After deposit, the acc_bal is : {Bank_Acc.Deposit(Bank_Acc)}")
# print(f"After withrawal,the acc_bal is :{Bank_Acc.Withdraw(Bank_Acc)}")
# print(f"After deposit and withdrawal,the total balance iss:{Bank_Acc.availablebalance(Bank_Acc)}")

# Class Person():
# def __init_(self,name,age,dept):
#     self.name = name
#     self.age = age
#     self.dept = dept
#     def General(self):
#         print(f"This is {self.name}, {self.age}yrs old, in dept")

#     class Student(person):
#         def lectures(self,level):
#             self.level = level
#             print(f"The student name is {self.name} {self.age}yrs old ,in dept {self.level}level")
#     class Lecturer(person):
#         def lecturers(self,course):
#             self.course = course
#             print(f"The lecturer name is{self.name} {self.age}yrs old in dept of {self.dept} taking {self.course} course")

#             person1 = Person('Ayo',31,"physics")
#             person2 = student("Enny", 70, "chemistry")
#             person3 = Lecturer("prof wale", 77, "accounting")
#             person1.Genral()
#             person2.student(500)
#             person3.lecturer()




      

    

# #  my_list = [2,'good']
# # our_list =[2,4,8]

# # class Car:
# #     def __init_(self,color,make,model):
# #         self.a = color
# #         self.b = make
# #         self.c = model
# #         print('new instance of car created')
# #     def describe(self):
# #         print(f'this is a {self.a} {self.b} {self.c}')

# # car1 = Car('blue', 'toyota','camry')
# # car2 = Car('white', 'honda' 'accord')
# # vehicle3 = Car('grey', 'lexus','jeep')

# # car1.describe()
# # vehicle3.describe()
# # print(vehicle3.color)
# # car2.describe()
# # car1.color = 'green'
# # car1.describe()
# # car1.make = 'venza'
# # car1.describe()

# class Animal():
#     def __init__(self,age,weight,height,colour):
#         self.age = age
#         self.weight = weight
#         self.height = height
#         self.color = colour
#     def describe(self):
#         print(f'this is a {self.age}yrs old {self.color} {self.weight} animal,with a height of {self.height}')

# class Mammal(Animal):
#     def describeMammal(self):
#         print(f'this is a {self.age}yrs old {self.color} {self.weight} mammal')

# cat1 =Mammal(3, '4kg', '15cm', 'blue')
# cat1.describe()
# cat1.describeMammal()

# a1 = Animal(5, '2kg', '15cm', 'black')
# a1.describe()
# a1.describeMammal

# print(a1.weight)
# a1.weight = '7kg'
# a1.describe()


class BankAccount:
    def __init__(self,account_name, account_number,initial_bal = 0):
        self.a = account_name
        self.b = account_number
        self.c = initial_bal

    def describe(self):
        print(self.a,self.b,self.c)
# 
    # def __str__(self):
    #     return str("An object of class BankAccount")
    
    # def __repr__(self):
    #     return repr(f"an object of class BankAccount,with name: {self.a}")

    def deposit(self, amount):
        self.c += amount
        print(f"deposit successful of {amount},your new balance is ${self.c}")

    def withdraw(self, amount): 
        if self.c < amount:
            print("insufficient fund")
            return
        print(f"withdrawal of amount is successful")
        self.c -= amount
        print(f"Theres a withdrawal of {amount}, your total balance is ${self.c}")


ACC1 = BankAccount('Alayo',44454)
ACC2 = BankAccount('NEEMAH',345524,345)

ACC1.withdraw(900)
ACC2.withdraw(40)
ACC1.describe()
ACC2.describe()

print(ACC1)
print(ACC2)

class Person:
    def __init__(self, name, age, height):
        pass