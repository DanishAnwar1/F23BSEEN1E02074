# Exercise 1: Calculate the multiplication and sum of two numbers

# Given two integer numbers, return their product only if the product is equal to or lower than
# 1000. Otherwise, return their sum.

# Given 1 :
# num1=20
# num2=30 
num1=20
num2=30
def calculate_product_or_sum(num1,num2):
    product=num1*num2 
    if product<=1000:
        return product
    else:
        sum=num1+num2 
        return sum
result=(calculate_product_or_sum(num1,num2))
print("Result:",result)
 

# Given 2:
# num1=40
# num2=30
num1=40
num2=30
def calculate_product_or_sum(num1,num2):
    product=num1*num2 
    if product<=1000:
        return product 
    else:
        sum=num1+num2 
        return sum
result=(calculate_product_or_sum(num1,num2)) 
print("Result:",result)


