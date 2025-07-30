def is_safe(report):
    diffs = [report[i+1] - report[i] for i in range(len(report)-1)]
    if any(abs(d) < 1 or abs(d) > 3 for d in diffs):
        return False
    if all(d > 0 for d in diffs):
        return True
    if all(d < 0 for d in diffs):
        return True
    return False

def is_safe_with_removal(report):
    if is_safe(report):
        return True
    # Essayer de retirer chaque élément un par un
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report):
            return True
    return False

safe_count = 0

with open('lvl2.txt', 'r') as f:
    for line in f:
        report = list(map(int, line.strip().split()))
        if is_safe_with_removal(report):
            safe_count += 1

print("Nombre de rapports sûrs avec le Problem Dampener :", safe_count)
