## Python - Almost a circle

#### Task 0: If it's not tested it doesn't work.
All your files, classes and methods must be unit tested and be PEP 8 validated.

#### Task 1:  Base class
Write the first class `Base`:

Create a folder named models with an empty file `__init__.py` inside - with this file, the folder will become a Python package

Create a file named models/base.py:
- Class `Base`:
	- private class attribute `__nb_objects = 0`
	- class constructor: `def __init__(self, id=None):`:
		- if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume `id` is an integer and you don’t need to test the type of it
		- otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`

This class will be the “base” of all other classes in this project. The goal of it is to manage `id` attribute in all your future classes and to avoid duplicating the same code.

#### Task 2: First Rectangle
Write the class `Rectangle` that inherits from `Base`:
- In the file `models/rectangle.py`
- Private instance attributes, each with its own public getter and setter:
	- `__width` -> `width`
	- `__height` -> `height`
	- `__x` -> `x`
	- `__y` -> `y`
- Class constructor: `def __init__(self, width, height, x=0, y=0, id=None):`
	- Call the super class with `id` - this super call with use the logic of the `__init__` of the `Base` class
	- Assign each argument `width`, `height`, `x` and `y` to the right attribute

#### Task 3: Validate attributes
Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):
- If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
- If `width` or `height` is under or equals 0, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
- If `x` or `y` is under 0, raise the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`

#### Task 4: Area first
Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.

#### Task 5: Display #0
Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle `x` and `y` here.

#### Task 6: `__str__`
Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`
