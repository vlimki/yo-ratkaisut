askeleet = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

xs = {}

for i,_ in askeleet:
    for j,_ in askeleet:
        for k,_ in askeleet:
            for l,_ in askeleet:
                x = i + j + k + l
                xs[x] = (xs.get(x) or 0) + 1

kaikki = sum(xs.values())
for k in xs.keys():
    print(f"P(x = {k}) = {xs[k]}/{kaikki} = {xs[k]/kaikki}")
