import re

with open("lvl3.txt", "r", encoding="utf-8") as f:
    data = f.read()

# Expressions régulières pour capturer les instructions
pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)")

enabled = True
total = 0

# Parcours du texte dans l'ordre
for match in pattern.finditer(data):
    if match.group(0) == "do()":
        enabled = True
    elif match.group(0) == "don't()":
        enabled = False
    elif match.group(1) and match.group(2) and enabled:
        x, y = int(match.group(1)), int(match.group(2))
        total += x * y

print(total)
