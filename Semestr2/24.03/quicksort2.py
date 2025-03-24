# sorted()

lista = [7,2,5,1,9]

def quickSort_mid(arr:list) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    pivot = arr[mid]

    lesser = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]

    return quickSort_mid(lesser) + [pivot] + quickSort_mid(greater)

import random
def quickSort_mid(arr:list) -> list:
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    lesser = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]

    return quickSort_mid(lesser) + [pivot] + quickSort_mid(greater)


def quickSort_mediana(arr:list) -> list:
    if len(arr) <= 1:
        return arr

    a, b, c = arr[0],arr[len(arr) // 2], arr[-1]

    if (a < b and b < c ) or (c < b and b < a):
        pivot = b
    elif (b < a and a < c ) or ( c < a and a < b):
        pivot = a
    else:
        pivot = c

    lesser = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]

    return quickSort_mediana(lesser) + [pivot] + quickSort_mediana(greater)


print(quickSort_mid(lista))