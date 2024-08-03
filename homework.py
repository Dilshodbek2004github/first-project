from os import system
import math
system("cls")
#------------------------------*100-ballik-Masala*-------------------------------------------------------------------------------
# def minSwaps(nums):
#     n, t = len(nums), sum(nums)
#     c = sum(nums[:t]); m = c
#     for i in range(t, n+t): c = c - nums[i-t] + nums[i%n]; m = max(m, c)
#     return t - m

# nums = [0, 1, 0, 1, 1, 0, 0]
# print(minSwaps(nums))  

# nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
# print(minSwaps(nums)) 

# nums = [1, 1, 0, 0, 1]
# print(minSwaps(nums))  
#-----------------------------1-Masala-----------------------------------------------------------------------------
# def print_primes(n):
#     if n < 2:
#         return
    
#     primes = [True] * (n + 1)
#     primes[0] = primes[1] = False
    
#     for i in range(2, int(n ** 0.5) + 1):
#         if primes[i]:
#             for j in range(i * i, n + 1, i):
#                 primes[j] = False
    
#     for i in range(n + 1):
#         if primes[i]:
#             print(i)

# print_primes(int(input("Son kiriting:\n")))
#----------------------------------2-Masala---------------------------------------------------------------------------------------------
# def round_up_numbers(numbers):
#     rounded_numbers = []
#     for num in numbers:
#         rounded_numbers.append(math.ceil(num))
#     return rounded_numbers

# original_numbers = [3.2, 4.7, 1.9, 7.0, 2.3]
# rounded_numbers = round_up_numbers(original_numbers)
# print("Original numbers:", original_numbers)
# print("Rounded up numbers:", rounded_numbers)
#------------------------------------3-Masala-------------------------------------------------------------------------------------------------------
# def get_integer_parts(numbers):
#     integer_parts = [int(num) for num in numbers]
#     return integer_parts

# real_numbers = [3.14, 2.71, 1.41, 0.58]
# integer_parts = get_integer_parts(real_numbers)
# print(integer_parts)  
#------------------------------------4-Masala----------------------------------------------------------------------------------------------------------------------------------------
# def map_function(x):
#     if x > 0:
#         return -x
#     else:
#         return 2 * x

# num = float(input("Enter a number: "))
# result = map_function(num)
# print("The result is:", result)
#----------------------------------5-Masala------------------------------------------------------------------------------------------------------
# def filter_cube(n):
#     result = []
#     for i in range(1, n+1):
#         if i**3 > n:
#             result.append(i)
#     return result

# n = int(input("N sonini kiriting: "))

# cube_greater_than_n = filter_cube(n)

# print(f"Kubidan katta sonlar ro'yxati: {cube_greater_than_n}")
#-----------------------------------6-Masala-------------------------------------------------------------------------------------------------------------
# def filter_integers(numbers):
    
#     return [num for num in numbers if isinstance(num, int)]


# user_input = [3.14, 2, 1.5, 4, 2.7, 5]
# integers = filter_integers(user_input)
# print(integers)  
#-----------------------------------------7-Masala---------------------------------------------------------------------------------------------------------------
# def filter_primes(numbers):
    
#     def is_prime(n):
#         if n < 2:
#             return False
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
    
#     return [n for n in numbers if is_prime(n)]

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# primes = filter_primes(numbers)
# print(primes)  
#-----------------------------------8-Masala-----------------------------------------------------------------------------------------------
# text = "apple banana cherry date elderberry fig grape"

# words = list(filter(None, text.split()))

# print(words)
#----------------------------------------9-Masala--------------------------------------------------------------------------------------------------
# def filter_positive_numbers(numbers):
#     positive_numbers = [num for num in numbers if num > 0]
#     return positive_numbers

# numbers = [-5, 0, 3, -2, 7, 1, -9, 4]
# positive_nums = filter_positive_numbers(numbers)
# print(positive_nums) 
#-----------------------------------10-Masala------------------------------------------------------------------------------------------------------------
# def convert_types(values):
#     result = []
#     for value in values:
#         if isinstance(value, int):
#             result.append(float(value))
#         elif isinstance(value, float):
#             result.append(int(value))
#         else:
#             result.append(value)
#     return result

# data = [1, 2.5, 3, 4.7, 5.0]

# converted_data = convert_types(data)

# print(converted_data)
#---------------------------------11-Masala--------------------------------------------------------------------------------------------
# arr = [1, 0, 1, 1, 0]
# bool_arr = list(map(lambda x: x == 1, arr))
# print(bool_arr)