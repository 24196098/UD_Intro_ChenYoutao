import random

user_input_range = input("please set a number of the lower boundry of the range which you want to guess:")
user_input_range2 = input("please set another number of the upper boundry of the range:")
r1=int(user_input_range)
r2=int(user_input_range2)

random.seed(a=None, version=2)
a=random.randint(r1,r2)
n=1

user_input = input("Guess a integer between " + str(r1) + " to " + str(r2) + ":")
number = int(user_input)

while (number!=a):
        print("Guess again:")
        user_input = input()
        number = int(user_input)
        n += 1
print("Congratulations!")
print("Guesses made:" + str(n))