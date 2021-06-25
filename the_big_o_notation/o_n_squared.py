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
