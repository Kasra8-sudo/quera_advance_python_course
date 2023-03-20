n = int(input())


def f(n):
    names = []
    for i in range(n):
        name = input()
        names.append(name)

    result = []
    for nam in names:
        temp = ''
        for letter in nam:
            if letter not in temp:
                temp += letter
        result.append(len(temp))

    return max(result)


print(f(n))
