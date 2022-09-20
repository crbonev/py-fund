# number_of_electrons = int(input())
# shell = 0
# shells = []
# while number_of_electrons > 2 * shell ** 2:
#     shell += 1
#     max_per_shell = 2 * (shell ** 2)
#     if number_of_electrons > max_per_shell:
#         number_of_electrons -= max_per_shell
#     else:
#         max_per_shell = number_of_electrons
#
#     shells.append(max_per_shell)
#
# if number_of_electrons > 0:
#     shells.append(number_of_electrons)
# print(shells)
#
# number_of_electrons = int(input())
# new_list = []
# current_shell = 0
#
# while 0 < number_of_electrons:
#
#     current_shell += 1
#     shell_max = 2 * current_shell ** 2
#
#     if number_of_electrons >= shell_max:
#         new_list.append(shell_max)
#         number_of_electrons -= shell_max
#     else:
#         new_list.append(number_of_electrons)
#         number_of_electrons = 0
#
# print(new_list)
#
number_of_electrons = int(input())


def electron_distribution(electrons):
    new_list = []
    current_shell = 0
    while 0 < electrons:

        current_shell += 1
        shell_max = 2 * current_shell ** 2

        if electrons >= shell_max:
            new_list.append(shell_max)
            electrons -= shell_max
        else:
            new_list.append(electrons)
            electrons = 0

    return new_list


print(electron_distribution(number_of_electrons))
