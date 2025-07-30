def similarity_score(left_list, right_list):
    # On calcule la fréquence des nombres dans la liste droite
    from collections import Counter
    right_counts = Counter(right_list)

    # Pour chaque nombre dans left_list, on multiplie par son nombre d'apparitions dans right_list
    total = 0
    for num in left_list:
        total += num * right_counts[num]
    return total

left = []
right = []

with open('input.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            left.append(int(parts[0]))
            right.append(int(parts[1]))

result = similarity_score(left, right)
print("Similarity score :", result)
