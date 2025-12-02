resets = 0
with open("Day1.input", "r") as f:
    total = 50 
    lines = f.readlines()
    for line in lines:
        if line[0] == "R":
            total = (total + int(line[1:]))%100
        else:
            total = (total + (100 - int(line[1:])))%100
        if total == 0:
            resets += 1
print(resets)