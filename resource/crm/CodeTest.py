def func1(num):
    if num <= 1:
        return

    list1 = []
    for i in range(num):
        list1.append(i)
        func1(i)

    return list1


a = func1(10)

print(a)
