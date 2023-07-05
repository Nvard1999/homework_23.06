# Write a function called merge that takes two already sorted lists of possibly different lengths, and merges them into a single sorted list. Do this without using the sort method.


def merge(lst1, lst2):
    sorted_list = []

    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            sorted_list.append(lst1.pop(0))
        else:
            sorted_list.append(lst2.pop(0))

    sorted_list.extend(lst1)
    sorted_list.extend(lst2)

    return sorted_list

lst1 = [1, 7, 15, 63, 42]
lst2 = [6, 95, 3, 26, 14, 5]
result = merge(lst1, lst2)
print(result)




# Write a function called int_str that, given an integer less than 1015, returns the name of the integer in English. As an example, int_str(123456) should return one hundred twenty-three thousand, four hundred fifty-six.








# Write a function called is_sorted that is given a list and returns True if the list is sorted and False otherwise. Do this without using the sort method.



def is_sorted(lst):
	for i in lst:
		if lst[i+1] > lst[i]:
			return True
		else:
			return False
num = [1,9,4,7,0]
print (is_sorted(num))



# Write a function called calculate_area that takes the radius of a circle as an argument. Inside the function, calculate the area of the circle (πr^2) and print it. Test the function by calling it with different radius values.


import math
def calculate_area(radius):
	area = math.pi * radius ** 2
	print("The area of the circle with radius",radius,"is:",area)
calculate_area(5.6)



# Create a global variable called counter and initialize it with 0. Write a function called increment_counter that increments the value of counter by 1 and prints the updated value. Call the function multiple times and observe the changes in the global variable.



counter = 0
def increment_counter():
	global counter
	counter += 1
	print("Updated counter",counter)
increment_counter()
increment_counter()
increment_counter()


# Write a function called outer_function that takes a parameter x. Inside outer_function, define another function called inner_function that multiplies x by a given factor. Call inner_function from outer_function and print the result.


def outer_function(x):
	def inner_function(factor):
		result = x * factor
		print("Result",result)
	inner_function(7)
outer_function(15)




# Create a global variable called x and set it to 10. Write a function called my_function that defines a local variable with the same name x and assigns it a value of 20. Inside the function, print the local x variable and the global x variable. Call my_function and observe the output.


x = 10
def my_function():
	x = 20
	print("Local x:",x)
	print("Global x:",globals()['x'])
my_function()



# Write a function called power_of that takes a parameter n and returns a function called power that calculates the nth power of a given number. Test the power_of function by calling it with different values of n and then using the returned power function to calculate powers.



def power_of(n):
	def power(i):
		return i ** n
	return power
power_square = power_of(2)
res_square = power_square(13)
print("Square",res_square) 
