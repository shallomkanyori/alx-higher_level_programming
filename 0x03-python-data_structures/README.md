## Python - Data Structures: Lists, Tuples

**Task 0: Print a list of integers.**
Write a function that prints all integers of a list.
- Prototype: `def print_list_integer(my_list=[]):`
- Format: one integer per line
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers

**Task 1: Secure access to an element in a list.**
Write a function that retrieves an element from a list like in C.
- Prototype: `def element_at(my_list, idx):`
- If `idx` is negative or if `idx` is out of range, the function should return None
- You are not allowed to import any module
- You are not allowed to use `try/except`

**Task 2: Replace element.**
Write a function that replaces an elment of a list at a specific position (like in C).
- Prototype: `def replace_in_list(my_list, idx, element):`
- If `idx` is negative of if `idx` is out of range, the function should not modify anything, and return the original list
- You are not allowed to import any module
- You are not allowed to use `try/except`

**Task 3: Print a list of integers... in reverse!**
Write a function that prints all integers of a list, in reverse order.
- Prototype: `def print_reversed_list_integer(my_list=[]):`
- Format: one integer per line
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers

**Task 4: Replace in copy.**
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
- Prototype: `def new_in_list(my_list, idx, element):`
- If `idx` is negative or out of range, the function should return a copy of the original list
- You are not allowed to import any module
- You are not allowed to use `try/except`

**Task 5: Can you C me now?**
Write a function that removes all characters `c` and `C` from a string.
- Prototype: `def no_c(my_string):`
- The function should return the new string
- You are not allowed to import any module
- You are not allowed to use `str.replace()`

**Task 6: Lists of lists = Matrix.**
Write a function that prints a matrix of integers.
- Prototype: `def print_matrix_integer(matrix=[[]]):`
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers

**Task 7: Tuples addition.**
Write a function that adds 2 tuples.
- Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
- Returns a tuple with 2 integers: The first element should be the addition of the first element of each argument. The second element should be the addition of the second element of each argument
- You are not allowed to import any module
- You can assume that the two tuples will only contain integers
- If a tuple is smaller than 2, use the value `0` for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers

**Task 8: More returns!**
Write a function that returns a tuple with the length of a string and its first character.
- Prototype: `def multiple_returns(sentence):`
- If the sentence is empty, the first character should be equal to `None`
- You are not allowed to import any module

**Task 9: Find the max.**
Write a function that finds the bigest integer of a list.
- Prototype: `def max_integer(my_list=[]):`
- If the list is empty, return `None`
- You can assume that the list only contains integers
- You are not allowed to import any module
- You are not allowed to use the builtin `max()`

**Task 10: Only by 2.**
Write a function that finds all multiples of 2 in a list.
- Prototype: `def divisible_by_2(my_list=[]):`
- Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
- The new list should have the same size as the original list
- You are not allowed to import any module

**Task 11: Delete at.**
Write a function that deletes the item at a specific position in a list.
- Prototype: `def delete_at(my_list=[], idx=0):`
- If `idx` is negative or out of range, nothing changes (return the same list)
- You are not allowed to use `pop()`
- You are not allowed to import any module

**Task 12: Switch.**
Complete the given source code in order to switch the value of `a` and `b`.
- You can find the source code [here](https://github.com/alx-tools/0x03.py/blob/master/12-switch_py)
- Your code should be inserted where the comment is (line 4)
- Your program should be exactly 5 lines long

**Task 13: Linked list palindrome.**
**Technical interview preparation**
Write a function in C that checks if a singly linked list is a palindrome.
- Prototype: `int is_palindrome(listint_t **head);`
- Return: `0` if it is not a palindrome, `1` if it is a palindrome
- An empty list is considered a palindrome
