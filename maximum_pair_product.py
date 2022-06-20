def get_maximum_product(num: int) -> int:
    str_num = str(num)
    result = []

    for i in range(1, len(str_num) - 1):
        for j in range(i + 1, len(str_num)):
            first = int(str_num[:i])
            second = int(str_num[i:j])
            third = int(str_num[j:])
            result.append(first * second * third)
    return max(result)


def test():
    number = 1234
    print(get_maximum_product(number))


if __name__ == '__main__' :
    test()
