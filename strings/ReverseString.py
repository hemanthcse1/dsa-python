

def reverse_string(str):
    chars = list(str)
    start = 0
    end = len(chars) -1

    while start < end:
        temp = chars[start]
        chars[start] = chars[end]
        chars[end] = temp

        start += 1
        end -= 1
    return ''.join(chars)

str = "hemanth"
reversed_string = reverse_string(str)
print(reversed_string)