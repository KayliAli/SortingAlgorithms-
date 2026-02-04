def quick_sort(ls):
    if len(ls) <= 1:
        return ls

    pivot = ls[len(ls) // 2]
    sol = []
    sag = []

    for i, eleman in enumerate(ls):
        if i == len(ls) // 2:
            continue
        if eleman < pivot:
            sol.append(eleman)
        else:
            sag.append(eleman)

    return quick_sort(sol) + [pivot] + quick_sort(sag)
