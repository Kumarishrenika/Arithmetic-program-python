# simple Python program that performs basic arithmetic operations:

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def floor_div(a,b):
    return a//b
def power(a,b):
    return a**b

a=int(input("enter first number: "))
b=int(input("enter second number: "))

output_add=add(a,b)
output_sub=sub(a,b)
output_mul=mul(a,b)
output_div=div(a,b)
output_mod=mod(a,b)
output_floor_div=floor_div(a,b)
output_power=power(a,b)
print(f"Sum is : {output_add}")
print(f"Sub is :{output_sub}")
print(f"mul is : {output_mul}")
print(f"div is : {output_div}")
print(f"modulo is : {output_mod}")
print(f"floor_division is : {output_floor_div}")
print(f"power is : {output_power}")

