"""
Bucle while
break y continue
"""

i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print()


# break
i = 0
while i < 10:
    print(i, end=" ")
    if i == 5:
        break
    i += 1
