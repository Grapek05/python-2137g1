# Przykładowa tablica reprezentująca drzewo binarne
tree = [1, 2, 3, 4, 5, 6, 7]

def get_left_child(index):
    """Zwraca lewe dziecko węzła o danym indeksie."""
    return 2 * index + 1


def get_right_child(index):
    """Zwraca prawe dziecko węzła o danym indeksie."""
    return 2 * index + 2


def get_parent(index):
    """Zwraca rodzica węzła o danym indeksie."""
    return (index - 1) // 2

# Dostęp do elementów drzewa
index = 0
left_child_index = get_left_child(index)
right_child_index = get_right_child(index)

print(f"Wartość korzenia: {tree[index]}")
print(f"Lewe dziecko korzenia: {tree[left_child_index]}")
print(f"Prawe dziecko korzenia: {tree[right_child_index]}")