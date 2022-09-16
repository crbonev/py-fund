# happiness = list(map(int, input().split(' ')))
# factor = int(input())
#
# happiness = [x*factor for x in happiness]
#
#
# # happiness = list(map(lambda x: int(x)*factor, happiness))
#
# filtered = list(filter(lambda x: x >= (sum(happiness) / len(happiness)), happiness))
#
# if len(filtered) >= len(happiness) / 2:
#     print(f'Score: {len(filtered)}/{len(happiness)}. Employees are happy!')
# else:
#     print(f"Score: {len(filtered)}/{len(happiness)}. Employees are not happy!")

command = ''
like = 0
dislike = 0
unlike = 0
while True:
    command = input()
    if command == 'like':
        like += 1
        print(f'Likes: {like} Dislikes: {dislike} Unliked: {unlike}')
    elif command == 'dislike':
        dislike += 1
        print(f'Likes: {like} Dislikes: {dislike} Unliked: {unlike}')
    elif command == 'unlike' and like > 0:
        like -= 1
        unlike += 1
        print(f'Likes: {like} Dislikes: {dislike} Unliked: {unlike}')
    elif command == 'justin bieber':
        dislike += 1000000
        unlike += like
        like = 0
        print(f'Likes: {like} Dislikes: {dislike} Unliked: {unlike}')
