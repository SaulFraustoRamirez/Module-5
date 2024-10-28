# Assignemnt 5
# Saul Frausto-Ramirez
# 10/22/2024

def print_hello(n):
    for _ in range(n):
        print("hello")

def print_hello_alt(n):
    print("hello\n" * n, end="")

    # TODO: There is another way without using loop but just print statement
    # 5 pts Extra credit
    pass

def print_hello_recursion(n):
    if n > 0:
        print("hello")
        print_hello_recursion(n - 1)

    # What about we use recursion?
    # 20 pts Extra credit
    # https://runestone.academy/ns/books/published/thinkcspy/IntroRecursion/toctree.html
    pass

def power_list(arr):
    for num in arr:
        print(num)

def power_list(arr):
    for num in arr:
        print(f"{num} {num**2}")

    # TODO: This is problem 2 in the handout
    # a. Write a loop that prints each of the numbers on a new line.
    # b. Write a loop that prints each number and its square on a new line.
    pass

def power_list_recursion(arr, index=0):
    if index < len(arr):
        print(f"{arr[index]} {arr[index]**2}")
        power_list_recursion(arr, index + 1)

    # TODO: This is problem 2 in the handout
    # Instead of looping, how about recursion?
    # 20 pts Extra credit
    pass

import turtle

def draw_building(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_skyline():
    turtle.speed(0)
    turtle.bgcolor("skyblue")

    # Draw buildings
    draw_building(-200, -100, 50, 200, "gray")
    draw_building(-140, -100, 60, 150, "darkgray")
    draw_building(-70, -100, 70, 250, "black")
    draw_building(10, -100, 50, 180, "gray")
    draw_building(70, -100, 60, 220, "darkgray")
    draw_building(150, -100, 50, 160, "black")

    # Draw the ground
    turtle.penup()
    turtle.goto(-300, -100)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()

draw_skyline()

"""
    Draws a regular polygon with the given parameters.

    Parameters:
    sides (int): The number of sides of the polygon.
    length (int): The length of each side of the polygon.
    line_color (str): The color of the polygon's outline (as a string, e.g., 'blue').
    fill_color (str): The color to fill the inside of the polygon (as a string, e.g., 'red').
    
    """
pass

def problem_4():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("Divisible by both")
        elif i % 3 == 0:
            print("Divisible by three")
        elif i % 5 == 0:
            print("Divisible by five")
        else:
            print(i)

    """
    Consider a program that iterates the integers from 1 to 50. For multiples of three
    print “Divisible by three” instead of the number and for the multiples of five print “Divisible by
    five”. For numbers which are multiples of both three and five print “Divisible by both”.
    """
    pass

def main():
    n = 100
    print_hello(n)
    print_hello_alt(n)
    print_hello_recursion(n)
    arr = [1, 2, 3, 4, 5]
    power_list(arr)
    power_list_recursion(arr)
    draw_polygon(5, 100, 'blue', 'red')
    problem_4()
    
main()