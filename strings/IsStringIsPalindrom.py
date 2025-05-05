

def is_palindrome(str_ex):

    start = 0
    end = len(str_ex) -1

    while start < end:
        if str_ex[start].lower() != str_ex[end].lower():
            return False
        start += 1
        end -= 1

    return True


string1 = "hemanth" # False
string = 'Madam' # True
print(is_palindrome(string))