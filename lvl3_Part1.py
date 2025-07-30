import re

def sum_of_muls(memory_str):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    matches = re.findall(pattern, memory_str)

    total = 0
    for x, y in matches:
        total += int(x) * int(y)
    return total


example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

print(sum_of_muls(example))  # Doit afficher 161

# Pour utiliser avec ton input réel, tu peux lire le fichier et passer le contenu à la fonction

with open("lvl3.txt") as f:
    corrupted_memory = f.read()

print(sum_of_muls(corrupted_memory))
 