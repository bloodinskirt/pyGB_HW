# Задача 26
"""
def power(n1, n2):
    if (n2 == 1):
        return (n1)
    if (n2 != 1):
        return (n1 * power(n1, n2 - 1))
n1 = int(input("Pls input number: "))
n2 = int(input("Pls input degree: "))
print("Result is - ", power(n1, n2))
"""

# Задача 28
"""
def sum(a, b):
    if a == 0:
        return b
    return sum(a - 1, b + 1)
"""