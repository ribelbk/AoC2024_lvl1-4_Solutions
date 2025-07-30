def is_safe(report):
    # Calcule les différences entre éléments consécutifs
    diffs = [report[i+1] - report[i] for i in range(len(report)-1)]
    
    # Vérifie que toutes les différences sont non nulles et entre 1 et 3 en valeur absolue
    if any(abs(d) < 1 or abs(d) > 3 for d in diffs):
        return False
    
    # Vérifie si tout est strictement croissant
    if all(d > 0 for d in diffs):
        return True
    
    # Vérifie si tout est strictement décroissant
    if all(d < 0 for d in diffs):
        return True
    
    return False

safe_count = 0

with open('lvl2.txt', 'r') as f:
    for line in f:
        report = list(map(int, line.strip().split()))
        if is_safe(report):
            safe_count += 1

print("Nombre de rapports sûrs :", safe_count)
