# 1. Declare your age as integer variable
age = int(input('age: '))
print(age)
# 2. Declare your height as a float variable
height = float(input('height: '))
print(height)
# 3. Declare a variable that store a complex number
com = complex(input("complex: "))
print(com)
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5*base*height
print("The higher of the triangle:",int(area))
#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a+b+c
print("The perimeter of the triangle:",float(perimeter))
#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length*width
print("The area of rectangle:",area)
perimeter = 2*(length+width)
print("The perimeter of rectangle:",perimeter)  
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = float(input("Enter r: "))
pi = 3.14
area = pi*r**2
circumference = 2*pi*r
print("Circumference:",circumference)
print("area:",area)
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# 9. 10. 11.
# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
a = "python"
b = "dragon"
print(len(a)!=len(b))
#13. Use and operator to check if 'on' is found in both 'python' and 'dragon', use 'in'
a = 'python'
b = 'dragon'
print("Check on in python:", 'on' in a)
print("Check on in dragon:",'on' in b)
#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
a = 'I hope this course is not full of jargon'
print("Check: ",'jargon' in a)
#15. There is no 'on' in both dragon and python, use "not in"
a = 'python'
b = 'dragon'
print("Check on not in python:", 'on' not in a)
print("Check on not in dragon:",'on' not in b)
#16. Find the length of the text python and convert the value to float and convert it to string
a = 'python'
print(len(a))
print(type(a))
b = float(len(a))
print(type(b))
c = str(b)
print(type(c))
#17. 
#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
a = 7//3
b = int(2.7)
print(a == b)
#19. Check if type of '10' is equal to type of 10
a = '10'
b = 10
print(a == b)
# 20. 
#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour:"))
print("Your weekly earning: ",hours*rate_per_hour)
#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = float(input("Enter number of years you have lived:"))
months = years*12
days = months*30
hours = days*24
minutes = hours*60
seconds = minutes*60
print("You have lived for",seconds,"seconds.")
#23. Write a Python script that displays the following table
print("1",         "1",         "1",         1 * 1,            1 * 1 * 1)
print("2",         "1",         "2",         2 * 2,            2 * 2 * 2)
print("3",         "1",         "3",         3 * 3,            3 * 3 * 3)
print("4",         "1",         "4",         4 * 4,            4 * 4 * 4)
print("5",         "1",         "5",         5 * 5,            5 * 5 * 5)




