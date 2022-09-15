lines = int(input())
word = input()
list1 = []
list2 = []
for n in range(lines):
    word1 = input()
    if word in word1:
        list2.append(word1)
    list1.append(word1)
print(list1)
print(list2)