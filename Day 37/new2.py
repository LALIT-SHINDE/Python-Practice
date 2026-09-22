for i in arr:
    count = 0

    if i not in new:

        for j in arr:
            if i == j:
                count += 1

        new += [i]
