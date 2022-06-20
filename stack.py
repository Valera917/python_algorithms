test_string = input('Enter the string: ')
stack = []
fl_verify = True

for char in test_string:
    if char in '([{':
        stack.append(char)
    elif char in ')]}':
        if not stack:
            flag_verify = False
            break

        last_el = stack.pop()
        if last_el == '(' and char == ')':
            continue
        if last_el == '[' and char == ']':
            continue
        if last_el == '{' and char == '}':
            continue

        fl_verify = False
        break


if fl_verify and not stack:
    print(True)
else:
    print(False)
