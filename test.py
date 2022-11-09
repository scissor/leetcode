subset = [1]
bits = [0, 1]


for i in range(2):
    subset +=  [x + 1 for x in subset]
    bits += subset

    print(subset)
    print(bits)