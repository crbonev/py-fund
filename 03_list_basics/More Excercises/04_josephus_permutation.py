main_list = input().split()
kill = int(input())
new_list = []
not_full = True
while len(main_list) != 0:

    for person in main_list:
        current = kill - 1
        if current > len(main_list):
            current -= len(main_list)
        new_list.append(main_list[current])
        main_list.remove(main_list[current])

        print(f'{main_list}main_list')
        print(f'{new_list}new_list')






