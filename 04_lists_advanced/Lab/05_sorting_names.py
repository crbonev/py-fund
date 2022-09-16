names = input().split(', ')
result = sorted(names, key=lambda neshto: (-len(neshto), neshto))

print(result)
