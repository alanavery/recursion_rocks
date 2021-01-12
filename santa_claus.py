houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]
houses2 = ['Alan\'s house']

# Iterative
# def deliver_presents(lst):
#     for element in lst:
#         print(f'Delivering presents to {element}.')


# Recursive
def deliver_presents(lst, title=0):
    title += 1
    if len(lst) == 1:
        return f'Elf {title} is delivering presents to {lst[0]}.'
    print(f'Elf {title} is a manager.')
    first_half = lst[:int(len(lst) / 2)]
    second_half = lst[int(len(lst) / 2):]
    return deliver_presents(first_half, title), deliver_presents(second_half, title)


print(deliver_presents(houses))
