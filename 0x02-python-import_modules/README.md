## Python - import & modules

**Task 0: Import a simple function from a simple file.**
Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.
- You have to use print function with string format to display integers.
- You must define `a = 1` and `b = 2`, each on its own line, and use those two variables as arguments when calling the functions `add` and `print`.
- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line.
- You can only use the word `add_0` once in your code.
- You are not allowed to use `*` for importing or `__import__`.
- Your code should not be executed when imported - by using `__import__`.

**Task 1: My first toolbox!**
Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.
- Do not use the function `print` (with string format to display integers) more than 4 times.
- You have to define `a = 10` and `b = 5` each on its own line, and use those two variables only, as arguments when calling functions (including `print`).
- Your program should call each of the imported functions: `add`, `sub`, `mul`, and `div`.
- The word `calculator_1` should be used only once in your file.
- You are not allowed to use `*` for importing or `__import__`.
- Your code should not be executed when imported.

**Task 2: How to make a script dynamic!**
Write a program that prints the number of and the list of its arguments.
- The output should be:
	- Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise)
	- followed by `:` (or `.` if no arguments were passed) followed by a new line
	- followed by (if at least one argument), one line per argument: the position of the argument (starting at `1`) followed by `:`, followed by the argument value and a new line.
- Your code should not be executed when imported.
