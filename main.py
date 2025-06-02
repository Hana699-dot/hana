import random
lower_case ="abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
combination = lower_case + upper_case + numbers 
length_of_password = 8
password = "".join(random.sample(combination, length_of_password))
print("The Generated Password is :" , password)