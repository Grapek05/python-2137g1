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


print(quickSort_mid(lista))