def countInBand(scores, low, high):
    def lower_bound(target):
        left = 0
        right = len(scores)

        while left < right:
            mid = (left + right) // 2

            if scores[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def upper_bound(target):
        left = 0
        right = len(scores)

        while left < right:
            mid = (left + right) // 2

            if scores[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left

    return upper_bound(high) - lower_bound(low)


scores = [35, 42, 42, 50, 58, 58, 58, 63, 71, 88]

print(countInBand(scores, 42, 58))
print(countInBand(scores, 90, 100))