## JavaScript - Objects, Scopes and Closures

#### Task 0
[0-rectangle.js](0-rectangle.js) exports an empty class `Rectangle` that defines a rectangle.
- Uses the `class` notation to define the class

#### Task 1
[1-rectangle.js](1-rectangle.js) contains a class `Rectangle` that defines a rectangle:
- Uses the `class` notation to define the class
- The constructor takes 2 arguments `w` and `h`
- The `width` instance attribute is initialized with the value of `w`
- The `height` instance attribute is initialized with the value of `h`

#### Task 2
[2-rectangle.js](2-rectangle.js) contains a class `Rectangle` that defines a rectangle:
- Uses the `class` notation to define the class
- The constructor takes 2 arguments `w` and `h`
- The `width` instance attribute is initialized with the value of `w`
- The `height` instance attribute is initialized with the value of `h`
- Creates an empty object if `w` or `h` is not a positive integer greater than 0

#### Task 3
[3-rectangle.js](3-rectangle.js) contains a class `Rectangle` that defines a rectangle:
- Uses the `class` notation to define the class
- The constructor takes 2 arguments `w` and `h`
- The `width` instance attribute is initialized with the value of `w`
- The `height` instance attribute is initialized with the value of `h`
- Creates an empty object if `w` or `h` is not a positive integer greater than 0
- Creates an instance method called `print()` that prints the rectangle using the character `X`

#### Task 4
[4-rectangle.js](4-rectangle.js) contains a class `Rectangle` that defines a rectangle:
- Uses the `class` notation to define the class
- The constructor takes 2 arguments `w` and `h`
- The `width` instance attribute is initialized with the value of `w`
- The `height` instance attribute is initialized with the value of `h`
- Creates an empty object if `w` or `h` is not a positive integer greater than 0
- Instance methods:
	- `print()` that prints the rectangle using the character `X`
	- `rotate()` that exchanges the `width` and the `height` of the rectangle
	- `double()` that multiplies the `width` and the `height` of the rectangle by 2

#### Task 5
[5-square.js](5-square.js) contains a class `Square` that defines a square and inherits from `Rectangle` of [4-rectangle.js](4-rectangle.js):
- Uses the `class` notation to define the class
- The constructor takes 1 argument: `size`
- The constructor calls the constructor of `Rectangle`

#### Task 6
[6-square.js](6-square.js) contains a class `Square` that defines a square and inherits from `Square` of [5-square.js](5-square.js):
- Instance method:
	- `charPrint(c)` - prints the square using the character `c` if not `undefined`. Otherwise, uses the character `X`.

#### Task 7
[7-occurrences.js](7-occurrences.js) contains a function that returns the number of occurrences of an element in a list.
- Prototype: `exports.nbOccurences = function (list, searchElement)`

#### Task 8
[8-esrever.js](8-esrever.js) contains a function that returns the reversed version of a list:
- Prototype: `exports.esrever = function (list)`
- Does not use the built-in method `reverse`
