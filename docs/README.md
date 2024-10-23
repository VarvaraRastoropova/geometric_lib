# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Code in circle.py
In this program, you need to find the area and perimeter of the circle using the formulas written above.

Import library to use the pi number.
``` import math ```
Creating a function that returns the value of the circle area.
```
def area(r):
return math.pi * r * r
```
Example of a function call:
```
>>> area(3)
28.274333882308138
```
Creating a function that returns the value of the circle perimeter.
```
def perimeter(r):
    return 2 * math.pi * r
```
Example of a function call:
```
>>> perimeter(3)
18.84955592153876
```

## Code in square.py
In this program, you need to find the area and perimeter of the square using the formulas written above.

Creating a function that returns the value of the square area.
```
def area(a):
    return a * a
```
Example of a function call:
```
>>> area(3)
9
```
Creating a function that returns the value of the square perimeter.
```
def perimeter(a):
    return 4 * a
```
Example of a function call:
```
>>> perimeter(3)
12
```

## Code in rectangle.py
In this program, you need to find the area and perimeter of the rectangle using the formulas written above.

Creating a function that returns the value of the rectangle area.
```
def area(a, b): 
    return a * b
```
Example of a function call:
```
>>> area(3, 4)
12
```
Creating a function that returns the value of the rectangle perimeter.
```
def perimeter(a, b): 
    return 2 * (a + b)
```
Example of a function call:
```
>>> perimeter(3, 4)
14
```

## Code in triangle.py
In this program, you need to find the area and perimeter of the triangle using the formulas written above.

Creating a function that returns the value of the triangle area.
```
def area(a, h): 
    return a * h / 2
```
Example of a function call:
```
>>> area(3, 4)
6.0
```
Creating a function that returns the value of the triangle perimeter.
```
def perimeter(a, b, c): 
    return a + b + c
```
Example of a function call:
```
>>> perimeter(3, 5, 5)
13
```

## Project modification history
Hash of the commit:
[b73a7c8eb0f82ef8e4da690d18a46c3fd152ac91](https://github.com/VarvaraRastoropova/geometric_lib/commit/b73a7c8eb0f82ef8e4da690d18a46c3fd152ac91)
File rectangle.py added.

Hash of the commit:
[f7712b336fdb978e1a26e741a161384b81ef1eb1](https://github.com/VarvaraRastoropova/geometric_lib/commit/f7712b336fdb978e1a26e741a161384b81ef1eb1)
The file rectangle.py corrected ```return a + b``` to ```return 2 * (a + b)``` because there was an incorrect formula.

Hash of the commit:
[8ba9aeb3cea847b63a91ac378a2a6db758682460](https://github.com/VarvaraRastoropova/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)
File circle.py added.
