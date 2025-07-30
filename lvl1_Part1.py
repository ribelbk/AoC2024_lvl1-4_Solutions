def total_distance(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    return sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

# Lire les données depuis le fichier 'lvl1.txt' dans le même dossier
left = []
right = []

with open('lvl1.txt', 'r') as f:
    for line in f:
        # On suppose que chaque ligne contient deux nombres séparés par espaces ou tabulations
        parts = line.strip().split()
        if len(parts) == 2:
            left.append(int(parts[0]))
            right.append(int(parts[1]))

result = total_distance(left, right)
print("Distance totale :", result)
