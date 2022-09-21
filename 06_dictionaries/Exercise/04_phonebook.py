dictionary = {}
searches = 0
while True:
    data = input().split('-')
    if len(data) < 2:
        searches = int(data[0])
        break
    dictionary[data[0]] = data[1]
while searches > 0:
    searches -= 1
    search = input()
    for key, value in dictionary.items():
        if search == key:
            print(f"{key} -> {value}")
    if search not in dictionary:
        print(f"Contact {search} does not exist.")