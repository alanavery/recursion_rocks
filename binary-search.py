def split(input, target):
    midpoint = len(input) // 2
    print(f'Searching {input} for the number {target}.')
    print(f'The midpoint is {midpoint}.')
    if len(input) <= 1:
        if input[0]['num'] == target:
            return f'\nSuccess! Your target of {target} has been found at index {input[0]["idx"]}'
        else:
            return f'\nSorry—your target of {target} was not found.'
    if input[midpoint]['num'] == target:
        return f'\nSuccess! Your target of {target} has been found at index {input[midpoint]["idx"]}'
    elif input[midpoint]['num'] > target:
        front_half = input[:midpoint]
        return split(front_half, target)
    else:
        back_half = input[midpoint:]
        return split(back_half, target)


def search(input, target):
    new_input = []
    idx = 0
    for element in input:
        dictionary = {
            'num': element,
            'idx': idx
        }
        idx += 1
        new_input.append(dictionary)
    return split(new_input, target)


print(search([1, 2, 3, 4, 6, 11, 56, 201, 455, 6678, 9001], 3))
