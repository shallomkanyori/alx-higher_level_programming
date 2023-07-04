## Python - Everything is object

**Task 0: Who am I?**
What function would you use to get the type of an object?
Write the name of the function in the file, without `()`.

**Task 1: Where are you?**
How do you get the variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without `()`.

**Task 2: Right count.**
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = 100
```

**Task 3: Right count=.**
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = 89
```

**Task 4: Right count=.**
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = a
```

**Task 5: Right count=+.**
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = a + 1
```

**Task 6: Is equal.**
What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

**Task 7: Is the same.**
What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

**Task 8: Is really equal.**
What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

**Task 9: Is really the same.**
What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

**Task 10: And with a list, is it equal.**
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```
