from mathutils.basic import add, subtract, multiply, divide
from mathutils.number import is_prime, is_armstrong, is_palindrome
from mathutils.statistics import mean, maximum, minimum

print("Arithmetic:", add(8, 2), subtract(8, 2), multiply(8, 2), divide(8, 2))
print("Number checks for 153:", is_prime(153), is_armstrong(153), is_palindrome(153))
values = [10, 20, 30, 40]
print("Statistics:", mean(values), maximum(values), minimum(values))
