num_of_characters = int(input())
total_sum = 0
for character in range(num_of_characters):
    current_character = input()
    total_sum += ord(current_character)         # ord() -> returns character ascii number
print(f'The sum equals: {total_sum}')           # str() return character by ascii number
