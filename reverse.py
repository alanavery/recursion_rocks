# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(input, already_reversed=''):
    if len(input) == 0:
        return already_reversed
    new_already_reversed = input[0] + already_reversed
    new_input = input[1:]
    return reverse(new_input, new_already_reversed)


print(reverse(""))
# => ""
print(reverse("a"))
# => "a"
print(reverse("ab"))
# => "ba"
print(reverse("computer"))
# => "retupmoc"
print(reverse(reverse("computer")))
# => "computer"
