from itertools import permutations
import re

# === INPUT DETAILS ===
names = ['john', 'doe', 'smith']  # fake names
dob = '01/01/1990'                # fake DOB
phone = '9876543210'              # fake phone number
symbols = ['@', '#', '$', '!', '_']
common_numbers = ['123', '1234', '007', '2024', '321']

# Extract DOB components
day, month, year = dob.split('/')
short_year = year[-2:]

# Build base words
base_words = set()

# Add name permutations
for i in range(1, len(names)+1):
    for combo in permutations(names, i):
        joined = ''.join(combo)
        base_words.add(joined)
        base_words.add(joined.capitalize())
        base_words.add(joined.upper())

# Add leetspeak-like variations
replacements = {'a': ['@', '4'], 'o': ['0'], 'i': ['1', '!'], 'e': ['3'], 's': ['$', '5']}

def mangle(word):
    combos = set()
    combos.add(word)
    for k, vals in replacements.items():
        for v in vals:
            if k in word:
                combos.add(word.replace(k, v))
    return combos

mangled_words = set()
for word in base_words:
    mangled_words.update(mangle(word))

# Add date and phone parts
extras = [year, short_year, month, day, phone[-4:], phone[-3:], *common_numbers]

# Combine all combos
final_words = set()
for base in mangled_words:
    final_words.add(base)
    for e in extras:
        final_words.add(base + e)
        final_words.add(e + base)
        for s in symbols:
            final_words.add(base + s + e)
            final_words.add(e + s + base)

# Save to file
with open("smart_wordlist.txt", "w") as f:
    for word in sorted(final_words):
        f.write(word + "\n")

print(f"[+] Wordlist generated: {len(final_words)} entries in smart_wordlist.txt")
