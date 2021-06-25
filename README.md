# Code with Mosh: Data Structures and Algorithms

## The boring stuff 💭

### What is it ❓

This repository serves as a collection of code snippets from "The Ultimate Data Structures and Algorithms", a course by Code with Mosh. An overview of his courses can be found found [here](https://codewithmosh.com/courses).

### Developer Information 🙋🏼‍♂️

Developed and written by Magnus Rødseth.

## The Big O Notation

### O(1)

```python
print("Hello, world!")  # O(1)
print("Hello, world again!")
# --> O(2) --> O(1) --> Constant time
```

### O(n)

```python
# ----- Example 1 -----
print("Hello, world!")  # O(1)

for i in range(10):  # O(n)
    print(i)

print("Bye, world!")  # O(1)

# ==> O(2 + n) ==> O(n)

# ----- Example 2 -----
numbers = [1, 2, 3]
names = ["John", "Adam", "Eve"]

for num in numbers:  # O(n)
    print(num)

for name in names:  # O(m)
    print(name)

# ==> O(n + m) ==> O(n)
# Still linear growth
```

### O(n^2)

```python
numbers = [1, 2, 3]

for first in numbers:  # O(n)
    for second in numbers:  # O(n)
        print(first + second)
# ==> O(n^2)

for num in numbers:  # O(n)
    print(num)
# ==> O(n + n^2) ==> O(n^2)

for first in numbers:  # O(n)
    for second in numbers:  # O(n)
        for third in numbers:  # O(n)
            print(first + second + third)
# ==> O(n^3)
```

### O(log n)

**Insert content here after learning about graphs and trees.**