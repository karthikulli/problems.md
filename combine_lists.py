def combine_lists(list1, list2):
    combined = sorted(list1 + list2, key=lambda x: x['positions'][0])
    result = []

    for elem in combined:
        l1, r1 = elem['positions']
        merged = False
        for r in result:
            l2, r2 = r['positions']
            overlap = max(0, min(r1, r2) - max(l1, l2))
            length1 = r1 - l1
            length2 = r2 - l2

            if overlap > length1 / 2 or overlap > length2 / 2:
                r['values'] += elem['values']
                merged = True
                break

        if not merged:
            result.append(elem)
    return result


list1 = [{"positions": [0, 4], "values": [1, 2]}]
list2 = [{"positions": [3, 7], "values": [3, 4]}]
print(combine_lists(list1, list2))
