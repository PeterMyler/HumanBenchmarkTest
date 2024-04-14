from math import sqrt
group = 3
curr_count = 1
changes = 0
rows = 3

for level in range(1, 90):
    if curr_count == group:
        rows += 1
        changes += 1
        curr_count = 0
        print()

    if changes == 3:
        changes = 0
        group += 2
        print()

    print(f"{level}: {rows}x{rows}")
    curr_count += 1
