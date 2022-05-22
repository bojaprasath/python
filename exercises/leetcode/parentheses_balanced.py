def check_parentheses(input):
    dict = {'{':'}', '(':')','[':']'}
    check_list = []
    for char in input:
        print(check_list)
        if char in dict.keys():
            check_list.append(char)
        elif char in dict.values():
            if len(check_list) > 1:
                if char != dict[check_list.pop()]:
                    return False
            else:
                return False
    return len(check_list) == 0


print(check_parentheses('(){}{}'))

print(check_parentheses(']'))