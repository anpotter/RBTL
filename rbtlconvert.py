# convert RBTL numeric identifiers to alpha

# test examples
exp = '((((((2 → 3) ∧ 2) → 3) → 1) ∧ (((2 → 3) ∧ 2) → 3)) → 1)'
#exp = '(((((((((3 → 2) ∧ 3) → 2) → 1) ∧ (((3 → 2) ∧ 3) → 2)) → 1) → ((((((¬(5 → ¬(((7 ∨ 6) ∧ ¬7) → 6)) → (((7 ∨ 6) ∧ ¬7) → 6)) ∧ ¬(5 → ¬(((7 ∨ 6) ∧ ¬7) → 6))) → (((7 ∨ 6) ∧ ¬7) → 6)) → 4) ∧ (((¬(5 → ¬(((7 ∨ 6) ∧ ¬7) → 6)) → (((7 ∨ 6) ∧ ¬7) → 6)) ∧ ¬(5 → ¬(((7 ∨ 6) ∧ ¬7) → 6))) → (((7 ∨ 6) ∧ ¬7) → 6))) → 4)) ∧ ((((((3 → 2) ∧ 3) → 2) → 1) ∧ (((3 → 2) ∧ 3) → 2)) → 1)) → ((((((¬(5 → ¬(((7 ∨ 6) ∧ ¬7) → 6)) → (((7 ∨ 6) ∧ ¬7) → 6)) ∧ ¬(5 → ¬(((7 ∨ 6) ∧ ¬7) → 6))) → (((7 ∨ 6) ∧ ¬7) → 6)) → 4) ∧ (((¬(5 → ¬(((7 ∨ 6) ∧ ¬7) → 6)) → (((7 ∨ 6) ∧ ¬7) → 6)) ∧ ¬(5 → ¬(((7 ∨ 6) ∧ ¬7) → 6))) → (((7 ∨ 6) ∧ ¬7) → 6))) → 4))'
print(exp)
print()

numlist = []
abc = []
c = 'a'

# initialize parallel lists

for i in range(1,27):
    numlist.append(i)
    abc.append(c)
    c = chr(ord(c) + 1)

# reverse order required to handle > 9 digits

numlist.reverse()
abc.reverse()

# replace digits with letters

for i in range(0,26):
    exp = exp.replace(str(numlist[i]),abc[i])
    i += 1    

print(exp)
print()
print(exp.upper())
