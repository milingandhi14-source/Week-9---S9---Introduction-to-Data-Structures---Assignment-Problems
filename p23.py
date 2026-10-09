def countPeriods(transactions, k):
    prefix_sum = 0
    count = 0

    frequency = {0: 1}

    for value in transactions:
        prefix_sum += value

        required = prefix_sum - k

        if required in frequency:
            count += frequency[required]

        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

    return count


transactions = [3, 4, -7, 1, 3, 3, 1, -4]
k = 7

print(countPeriods(transactions, k))

print(countPeriods([1, 2, 3], 10))