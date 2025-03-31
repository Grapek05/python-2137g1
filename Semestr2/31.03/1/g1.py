def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] # Wybieramy środkowy element jako pivot
    left = [x for x in arr if x < pivot] # Elementy mniejsze niż pivot
    middle = [x for x in arr if x == pivot] # Elementy równe pivotowi
    right = [x for x in arr if x > pivot] # Elementy większe niż pivot
    return quicksort(left) + middle + quicksort(right)

# Test
arr = [5, 3, 1, 6, 2, 3, 4, 1]
sorted_array = quicksort(arr)
# print(sorted_array) # Wynik: [1, 2, 3, 4, 5, 6, 7, 8]

# Test
# dodajemy indexowanie w liście

def quicksort2(arr):
    arr = [(value, index) for index, value in enumerate(arr)]
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][0] # Wybieramy środkowy element jako pivot
    left = [x for x in arr if x[0] < pivot] # Elementy mniejsze niż pivot
    middle = [x for x in arr if x[0] == pivot] # Elementy równe pivotowi
    right = [x for x in arr if x[0] > pivot] # Elementy większe niż pivot
    return [x[0] for x in quicksort(left)] + [x[0] for x in middle] + [x[0] for x in quicksort(right)]

# Zadanie: sortuj po nazwiskach

employees = [
    {"first_name": "Anna", "last_name": "Kowalska", "age": 29},
    {"first_name": "Jan", "last_name": "Nowak", "age": 34},
    {"first_name": "Marek", "last_name": "Kowalski", "age": 25},
    {"first_name": "Zofia", "last_name": "Nowak", "age": 29}
]

def quicksort3(arr, sortBy):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][sortBy]
    left = [x for x in arr if x[sortBy] < pivot]
    middle = [x for x in arr if x[sortBy] == pivot]
    right = [x for x in arr if x[sortBy] > pivot]
    return quicksort3(left, sortBy) + middle + quicksort3(right, sortBy)

sorted_employees = quicksort3(employees, "last_name")
print(sorted_employees)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] # Wybieramy środkowy element jako pivot
    left = [x for x in arr if x < pivot] # Elementy mniejsze niż pivot
    middle = [x for x in arr if x == pivot] # Elementy równe pivotowi
    right = [x for x in arr if x > pivot] # Elementy większe niż pivot
    return quicksort(left) + middle + quicksort(right)

# Test
arr = [5, 3, 1, 6, 2, 3, 4, 1]
sorted_array = quicksort(arr)
# print(sorted_array) # Wynik: [1, 2, 3, 4, 5, 6, 7, 8]

# Test
# dodajemy indexowanie w liście

def quicksort2(arr):
    arr = [(value, index) for index, value in enumerate(arr)]
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][0] # Wybieramy środkowy element jako pivot
    left = [x for x in arr if x[0] < pivot] # Elementy mniejsze niż pivot
    middle = [x for x in arr if x[0] == pivot] # Elementy równe pivotowi
    right = [x for x in arr if x[0] > pivot] # Elementy większe niż pivot
    return [x[0] for x in quicksort(left)] + [x[0] for x in middle] + [x[0] for x in quicksort(right)]

# Zadanie: sortuj po nazwiskach

employees = [
    {"first_name": "Anna", "last_name": "Kowalska", "age": 29},
    {"first_name": "Jan", "last_name": "Nowak", "age": 34},
    {"first_name": "Marek", "last_name": "Kowalski", "age": 25},
    {"first_name": "Zofia", "last_name": "Nowak", "age": 29}
]

# last_name, age

def quicksort3(arr, sortBy, sortAge=None):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][sortBy]
    left = [x for x in arr if x[sortBy] < pivot]
    middle = [x for x in arr if x[sortBy] == pivot]
    right = [x for x in arr if x[sortBy] > pivot]
    
    if sortAge and middle: middle = quicksort3(middle, "age")
    
    return quicksort3(left, sortBy, sortAge) + middle + quicksort3(right, sortBy, sortAge)

sorted_employees = quicksort3(employees, "last_name", "age")
print(sorted_employees)


arr = [4,2,2,8,3,3,1]
#Counting sort
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val+1)

    # zliczanie wystapień elementów
    for num in arr:
        count[num] +=1

    #rekonstrukcja posortowanej listy
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i]*count[i])

    return sorted_arr


# napisz funkcje ktora sortuje oceny studentow w akresie od 0 do 100
# wartosci wchodzace, lista ocen, min wartosc, max wartosc
# wyjscie - posortowane oceny


oceny = [88, 92, 75, 83, 90, 92, 60, 85, 90]

def grade_sort(arr, min_val, max_val):
    count = [0] * (max_val - min_val + 1)
    for grade in arr:
        count[grade - min_val] += 1
    sorted_grades = []
    for i in range(len(count)):
        sorted_grades.extend([i + min_val] * count[i])
    return sorted_grades

sorted_oceny = grade_sort(oceny, 0, 100)
print(sorted_oceny)