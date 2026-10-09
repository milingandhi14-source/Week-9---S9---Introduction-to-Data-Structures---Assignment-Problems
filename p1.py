def footfallReport(visitors, queries):
    prefix = [0] * (len(visitors) + 1)

    for i in range(len(visitors)):
        prefix[i + 1] = prefix[i] + visitors[i]

    result = []

    for start, end in queries:
        total = prefix[end + 1] - prefix[start]
        result.append(total)

    return result


visitors = [12, 7, 3, 9, 15, 4, 8]
queries = [(0, 2), (2, 5), (4, 6), (3, 3)]

print(footfallReport(visitors, queries))