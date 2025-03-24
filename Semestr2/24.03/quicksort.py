# sorted()

lista = [7,2,5,1,9]

def quickSort(arr:list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[0] # wybieranie pierwszego elementu
    lesser = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]

    return quickSort(lesser) + [pivot] + quickSort(greater)

print(quickSort(lista))