def abubblesort(list):
    n = len(list)

    for i in range(n):
        swapped = 0
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped += 1
        if swapped == 0:
            break
    return list

list = [12,32,56,32,11,67,89]
slist = abubblesort(list)
print(slist)