"""
Program Name: Geometry Calculator
Author: Kishan Atada
Purpose: Calculate the area, circumference, and perimeter of shapes.
Date: June 17, 2026

"""
import circle as c
import rectangle as r
# Aliases are used because somtimes multiple modules contain a same named function
# So, using alias makes it clear which module's function is being called.


while True:
    print('')
    print('Geometry Calaculator')
    print('---------------------')
    print('1. Calculate Circle Area')
    print('2. Calculate Circle Circumference')
    print('3. Calculate Rectangle Area')
    print('4. Calculate Rectangle Perimeter')
    print('5. Exit')
    print('')
    user_choice = int(input('Enter your choice (1-5): '))
    if user_choice == 1:
        radius = float(input('Enter the radius of the circle: '))
        print('') 
        print(f'The area of the circle is {c.calc_area(radius)} ')
    elif user_choice == 2:
        radius = float(input('Enter the radius of the circle: '))
        print('') 
        print(f'The circumference is {c.calc_circumference(radius)}')
    elif user_choice == 3:
        width = float(input('Enter the width of the rectangle: '))
        height = float(input('Enter the height of the rectangle:'))
        print('')  
        print(f'The area of the rectangle is {r.calc_area(width, height)} ')
    elif user_choice == 4:
        width = float(input('Enter the width of the rectangle: '))
        height = float(input('Enter the height of the rectangle:'))  
        print('') 
        print(f'The perimeter of the rectangle is {r.calc_perimeter(width, height)} ')
    elif user_choice == 5:
        print('Goodbye !')
        break
    print('')
    input('Press Enter to continue...')

