string = input()
lower_string = string.lower()
string_list = []
appear = 0
string_names = ["Water", "Sun", "Fish", "Sand"]

for lower in string_names:
    string_list.append(lower.lower())


for index in range(len(string_list)):
    new = string_list[index]
    appear += lower_string.count(new)
print(appear)
