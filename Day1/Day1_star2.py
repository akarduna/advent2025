resets = 0
with open("Day1.input", "r") as f:
    total = 50 
    lines = f.readlines()
    for line in lines:
        rotations = int(line[1:])
        resets += rotations // 100
        rotations = rotations%100
        start_total = total
        if line[0] == "R":
            total = (total + rotations)%100
            if total < start_total:
                resets += 1
        else:
            total = (total + (100 - rotations))%100
            if total > start_total and start_total != 0:
                resets += 1
            if total == 0:
                resets += 1
print(resets)