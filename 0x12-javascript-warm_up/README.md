## JavaScript - Warm up

#### Task 0
[0-javascript_is_amazing.js](0-javascript_is_amazing.js) is a JS script that prints 'JavaScript is amazing'.
- Uses constant variable `myVar` with the required value
- Uses `console.log(...)` to print the output

#### Task 1
[1-multi_languages.js](1-multi_languages.js) is a script that prints 3 lines using `console.log(...)`:
- First: "C is fun"
- Second: "Python is cool"
- Third: "JavaScript is amazing"

#### Task 2
[2-arguments.js](2-arguments.js) is a script that prints a message depending of the number of arguments passed:
- If no arguments are passed to the script, prints “No argument”
- If only one argument is passed to the script, prints “Argument found”
- Otherwise, prints “Arguments found”
- Uses `console.log(...)` to print all output

#### Task 3
[3-value_argument.js](3-value_argument.js) is a script that prints the first argument passed to it:
- If no arguments are passed to the script, prints “No argument”
- Uses `console.log(...)` to print all output
- Does not use `length`

#### Task 4
[4-concat.js](4-concat.js) is a script that prints two arguments passed to it, in the following format: “ is ”
- Uses `console.log(...)` to print all output

#### Task 5
[5-to_integer.js](5-to_integer.js) a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:
- If the argument can’t be converted to an integer, prints “Not a number”
- Uses `console.log(...)` to print all output
- Does not use `try/catch`

#### Task 6
[6-multi_languages_loop.js](6-multi_languages_loop.js) is a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop
- The first line: “C is fun”
- The second line: “Python is cool”
- The third line: “JavaScript is amazing”
- Uses `console.log(...)` to print all output
- Does not use any `if/else` statement
- Uses only one `console.log`

#### Task 7
[7-multi_c.js](7-multi_c.js) is a script that prints `x` times “C is fun”
- Where `x` is the first argument of the script
- If the first argument can’t be converted to an integer, prints “Missing number of occurrences”
- Uses `console.log(...)` to print all output
- Uses only two `console.log`

#### Task 8
[8-square.js](8-square.js) is a script that prints a square
- The first argument is the size of the square
- If the first argument can’t be converted to an integer, prints “Missing size”
- Uses the character `X` to print the square
- Uses `console.log(...)` to print all output

#### Task 9
[9-add.js](9-add.js) is a script that prints the addition of 2 integers
- The first argument is the first integer
- The second argument is the second integer
- Defines a function with this prototype: `function add(a, b)`
- Uses `console.log(...)` to print all output

#### Task 10
[10-factorial.js](10-factorial.js) is a script that computes and prints a factorial
- The first argument is an integer (argument can be cast as integer) used for computing the factorial
- Factorial of `NaN` is `1`
- Uses a recursive function
- Uses `console.log(...)` to print all output

#### Task 11
[11-second_biggest.js](11-second_biggest.js) is a script that searches for the second biggest integer in the list of arguments.
- Assumes all arguments can be converted to integer
- If no argument passed, prints `0`
- If the number of arguments is `1`, prints `0`

#### Task 12
[12-object.js](12-object.js) updates a script to replace an object's property `value` that was `12` with the value `89`.

#### Task 13
[13-add.js](13-add.js) contains a function that returns the addition of 2 integers.
- The function is visible from outside
- The function's name is add


#### Task 14
[100-let_me_const.js](100-let_me_const.js) modifies the value of `myVar` to `333`.
```
$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
$ ./100-main.js
333
```

#### Task 15
[101-call_me_moby.js](101-call_me_moby.js) contains a function that executes `x` times a function.
- The function is visible from outside
- Prototype: `function (x, theFunction)`
