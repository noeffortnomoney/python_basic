# Ngày 2: Biến - 30 ngày lập trình python
# 3. Declare a first name variable and assign a value to it
first_name = "Bình"
print("Bài tập 3")
print('first name: ',first_name)
print(type(first_name))
# 4. Declare a last name variable and assign a value to it
last_name = "Trương"
print("bài tập 4")
print('last name: ',last_name)
print(type(last_name))
# 5. Declare a full name variable and assign a value to it
full_name = "Trương Quốc Bình"
print("bài tập 5")
print('full name: ',full_name)
print(type(full_name))
# 6. Declare a country variable and assign a value to it
country = "Vietnam"
print("bài tập 6")
print('country: ',country)
print(type(country))
# 7. Declare a city variable and assign a value to it
city = "Hồ Chí Minh"
print("bài tập 7")
print('city: ',city)
print(type(city))
# 8. Declare an age variable and assign a value to it
age = 22
print("bài tập 8")
print('age: ',age)
print(type(age))
# 9. Declare a year variable and assign a value to it
year = 2001
print("bài tập 9")
print('year: ', year)
print(type(year))
#10. Declare a variable is_married and assign a value to it
is_married = True #viet hoa true/false
print("bài tập 10 ")
print("Is married?" ,is_married)
print(type(is_married))
#11. Declare a variable is_true and assign a value to it
is_true = False
print("bài tập 11")
print("Is true? ",is_true)
print(type(is_true))
#12. Declare a variable is_light_on and assign a value to it
is_light_on = False
print("bài tập 12")
print("Is light on? ",is_light_on)
print(type(is_light_on))
#13. Declare multiple variable on one line
multiple = "Bình", True, 22         #tuple
print("bài tập 13")
print("multiple: ",multiple)
print(type(multiple))
#lv2.1 Check the data type of all your variables using type() built-in function
print("Level 2.1")
print("oke") #đã làm
#lv2.2 Using the len() built-in function, find the length of your first name
print("Level 2.2")
print(len(first_name))
#lv2.3 Compare the length of your first name and your last name
print("Level 2.3")
print(len(last_name))
print(len(first_name) != len(last_name)) #true
#lv2.4 Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
add = num_one + num_two 
print("add: ",add)
# Subtract num_two from num_one and assign the value to a variable diff
subtract = num_one - num_one
print('subtract: ',subtract)
# Multiply num_two and num_one and assign the value to a variable product
multiply = num_one*num_two
print('multiply: ',multiply)
# Divide num_one by num_two and assign the value to a variable division
divide = num_one/num_two
print('divide: ',divide)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two%num_one
print('remainder: ',remainder)
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one**num_two #use pow()
print("exp: ",exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one//num_two #use // = floor division = phép chia phần nguyên
print('floor_division: ',floor_division)
#lv 2.5 The radius of a circle is 30 meters.
r = 30 
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = r**2*3.14
print("area of circle: ",area_of_circle)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = r*2*3.14
print("circum of circle: ",circum_of_circle)
# Take radius as user input and calculate the area.
r = float(input("Bán kính hình tròn: "))
print("Diện tích hình tròn: ",r**2*3.14)
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
name = str(input("Tên: "))
country = str(input("Thành phố: "))
age = int(input("Tuổi: "))
print(name,'-',country,'-',age)





