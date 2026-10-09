def longestStreak(costs, budget):
    left = 0
    current_sum = 0
    max_length = 0
    start_index = -1

    for right in range(len(costs)):
        current_sum += costs[right]

        while current_sum > budget:
            current_sum -= costs[left]
            left += 1

        length = right - left + 1

        if length > max_length:
            max_length = length
            start_index = left

    return (max_length, start_index)


costs = [4, 2, 1, 7, 3, 1, 2, 1, 5]
budget = 8

print(longestStreak(costs, budget))

print(longestStreak([9, 10], 8))