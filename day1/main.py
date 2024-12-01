from collections import defaultdict

datal = []
datar = []
sim_r = defaultdict(int)

with open("input.txt", "r") as f:
    for line in f.readlines():
        l, r = line.split()
        l, r = int(l), int(r)
        datal.append(l)
        datar.append(r)
        sim_r[r] += 1

datal = sorted(datal)
datar = sorted(datar)

sum = 0
sim = 0
for l, r in zip(datal, datar):
    sum += abs(l - r)
    sim += l * sim_r[l]


print(sum)
print(sim)

