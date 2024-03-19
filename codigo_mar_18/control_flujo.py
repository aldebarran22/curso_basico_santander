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

print()

# continue
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i, end=" ")

# Bucle infinito, se corta con control+C
while True:
    pass
