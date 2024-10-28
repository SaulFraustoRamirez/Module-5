# Assignment 5
**Author**: Saul Frausto-Ramirez  
**Date**: 10/22/2024

## Description
This assignment includes various Python functions to demonstrate iteration, recursion, and the use of the `turtle` module for drawing graphics. The functions cover tasks such as printing messages, calculating powers, and drawing a skyline.

## Functions

### `print_hello(n)`
Prints "hello" `n` times using a loop.

### `print_hello_alt(n)`
Prints "hello" `n` times using a single print statement. (Extra credit: Implement without a loop)

### `print_hello_recursion(n)`
Prints "hello" `n` times using recursion. (Extra credit: Implement using recursion)

### `power_list(arr)`
Prints each number in the list `arr` on a new line. Also prints each number and its square on a new line.

### `power_list_recursion(arr, index=0)`
Prints each number in the list `arr` and its square using recursion. (Extra credit: Implement using recursion)

### `draw_building(x, y, width, height, color)`
Draws a building at the specified coordinates with the given dimensions and color using the `turtle` module.

### `draw_skyline()`
Draws a skyline with multiple buildings and a ground using the `turtle` module.

### `problem_4()`
Iterates through integers from 1 to 50 and prints:
- "Divisible by three" for multiples of three
- "Divisible by five" for multiples of five
- "Divisible by both" for multiples of both three and five

## Usage
To run the assignment, execute the `main()` function. This will call all the defined functions and demonstrate their functionality.

```python
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
